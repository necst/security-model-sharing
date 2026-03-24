#!/usr/bin/env python3
"""
Vulnerability PoC — Automated Test Runner

Builds Docker images, runs each PoC inside a container, and checks whether
a new shell was spawned by the exploit.

Detection: we set a local (non-exported) bash variable _VULN_CANARY.
If the exploit spawns a new shell, that shell does NOT have the variable,
so `echo CHECK:$_VULN_CANARY` prints "CHECK:" (empty).  If no new shell
was spawned, we see "CHECK:<canary_value>".
"""

import os
import select
import subprocess
import sys
import time
import uuid

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
CANARY = f"CANARY_{uuid.uuid4().hex[:16]}"
TIMEOUT = int(os.environ.get("POC_TIMEOUT", 120))
READY = "__READY__"

TESTS = [
    # (name, directory, poc_script, has_input)
    ("KV1", "KV1", "poc_load.py", False),
    ("KV2", "KV2", "poc_load.py", False),
    ("KV3", "KV3", "poc_load.py", False),
    ("SV1", "SV1", "poc_load.py", True),
    ("SV2", "SV2", "poc_load.py", True),
    ("SV3", "SV3", "poc.py",      False),
]

RED    = "\033[0;31m"
GREEN  = "\033[0;32m"
YELLOW = "\033[1;33m"
CYAN   = "\033[0;36m"
BOLD   = "\033[1m"
NC     = "\033[0m"


def separator():
    print(f"{BOLD}{'━' * 60}{NC}")


def send(proc, line):
    proc.stdin.write((line + "\n").encode())
    proc.stdin.flush()


def send_and_wait(proc, cmd, timeout=30):
    """Send cmd + a ready marker, wait until the marker appears in output."""
    send(proc, cmd)
    send(proc, f"echo {READY}")
    return read_until(proc, READY, timeout)


def read_until(proc, marker, timeout=30):
    """Read stdout until `marker` appears or timeout. Returns (buf, found)."""
    buf = ""
    deadline = time.monotonic() + timeout
    fd = proc.stdout.fileno()
    while time.monotonic() < deadline:
        remaining = deadline - time.monotonic()
        if remaining <= 0:
            break
        ready, _, _ = select.select([fd], [], [], min(remaining, 0.5))
        if ready:
            chunk = os.read(fd, 4096)
            if not chunk:
                break
            buf += chunk.decode("utf-8", errors="replace")
            if marker in buf:
                return buf, True
    return buf, False


def drain(proc, timeout=0.5):
    """Read any remaining output."""
    buf = ""
    deadline = time.monotonic() + timeout
    fd = proc.stdout.fileno()
    while time.monotonic() < deadline:
        remaining = deadline - time.monotonic()
        if remaining <= 0:
            break
        ready, _, _ = select.select([fd], [], [], min(remaining, 0.1))
        if ready:
            chunk = os.read(fd, 4096)
            if not chunk:
                break
            buf += chunk.decode("utf-8", errors="replace")
    return buf


def build_image(name, vuln_dir):
    docker_dir = os.path.join(SCRIPT_DIR, vuln_dir, "docker")
    with open(os.path.join(docker_dir, "run.sh")) as f:
        lines = f.readlines()
    build_lines = []
    for line in lines:
        if "docker run" in line:
            break
        build_lines.append(line)
    result = subprocess.run(
        ["bash", "-c", "".join(build_lines)],
        cwd=docker_dir, capture_output=True, text=True, timeout=300,
    )
    return result.returncode == 0, result.stdout + result.stderr


def run_test(name, vuln_dir, poc_script, has_input):
    image_name = name.lower()

    print()
    separator()
    print(f"{BOLD}[TEST] {CYAN}{name}{NC}")
    separator()

    # ── Build ────────────────────────────────────────────────────────────
    print(f"  {CYAN}Building{NC} image '{image_name}'...")
    try:
        ok, build_out = build_image(name, vuln_dir)
    except subprocess.TimeoutExpired:
        print(f"  {RED}[FAIL]{NC} {name} — build timed out")
        return False, "build timeout"
    if not ok:
        print(f"  {RED}[FAIL]{NC} {name} — build failed")
        for l in build_out.strip().splitlines()[-5:]:
            print(f"    {l}")
        return False, "build error"
    print("  Image ready.")

    # ── Start container ──────────────────────────────────────────────────
    print(f"  {CYAN}Running{NC} PoC '{poc_script}' (timeout {TIMEOUT}s)...")
    proc = subprocess.Popen(
        ["docker", "run", "--rm", "-i", "-w", "/poc", image_name, "bash"],
        stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.STDOUT,
    )
    os.set_blocking(proc.stdout.fileno(), False)
    all_output = ""

    try:
        # Set canary (local, NOT exported) and confirm bash is alive
        out, ok = send_and_wait(proc, f"_VULN_CANARY={CANARY}", timeout=30)
        all_output += out
        if not ok:
            raise RuntimeError("Bash not responding")

        # Run the PoC.  Don't append a READY marker here — the PoC spawns
        # a shell so our marker would be consumed by the wrong process.
        send(proc, f"python -u {poc_script}")

        # If PoC calls input(), wait for the prompt text then send enter
        if has_input:
            out, ok = read_until(proc, "Press enter", timeout=60)
            all_output += out
            if not ok:
                raise RuntimeError("Never saw 'Press enter'")
            send(proc, "")

        # The exploit should spawn a shell.  The spawned shell is waiting
        # on stdin.  Give it a moment, then probe.
        time.sleep(3)

        # Probe: echo the canary.  The spawned shell (if any) does NOT
        # have _VULN_CANARY so it prints "CHECK:".
        send(proc, "echo CHECK:$_VULN_CANARY")
        out, ok = read_until(proc, "CHECK:", timeout=15)
        all_output += out

        # Grab rest of the CHECK line
        all_output += drain(proc, timeout=1)

        # Exit shells
        send(proc, "exit")
        time.sleep(0.2)
        send(proc, "exit")
        try:
            proc.wait(timeout=5)
        except subprocess.TimeoutExpired:
            proc.kill()

    except RuntimeError as e:
        proc.kill()
        try:
            rest, _ = proc.communicate(timeout=5)
            all_output += rest.decode("utf-8", errors="replace")
        except Exception:
            pass
        print(f"  {RED}[FAIL]{NC} {name} — {e}")
        print(f"        {YELLOW}Last 10 lines:{NC}")
        for l in all_output.strip().splitlines()[-10:]:
            print(f"        {l}")
        return False, str(e)

    # ── Analyse ──────────────────────────────────────────────────────────
    # Look for "CHECK:" followed by end-of-line (empty canary = spawned shell)
    # vs "CHECK:<canary>" (original bash, no new shell).
    # The CHECK: may appear mid-line (e.g. after "Press enter..." text).
    has_empty_check = "CHECK:\n" in all_output or all_output.rstrip().endswith("CHECK:")
    has_canary_check = f"CHECK:{CANARY}" in all_output
    lines = all_output.splitlines()
    
    if has_empty_check:
        print(f"  {GREEN}[PASS]{NC} {name} — New shell spawned")
        return True, "pass"
    elif has_canary_check:
        print(f"  {RED}[FAIL]{NC} {name} — No new shell (canary present)")
        return False, "no shell spawned"
    elif any("CHECK:" in l for l in lines):
        print(f"  {RED}[FAIL]{NC} {name} — Unexpected CHECK content")
        for l in lines:
            if "CHECK:" in l:
                print(f"        {l.strip()}")
        return False, "unexpected marker"
    else:
        print(f"  {RED}[FAIL]{NC} {name} — No CHECK marker")
        print(f"        {YELLOW}Last 10 lines:{NC}")
        for l in lines[-10:]:
            print(f"        {l}")
        return False, "no marker"


def main():
    print(f"{BOLD}╔══════════════════════════════════════════════════════════════╗{NC}")
    print(f"{BOLD}║          Vulnerability PoC — Automated Test Runner           ║{NC}")
    print(f"{BOLD}╚══════════════════════════════════════════════════════════════╝{NC}")
    print()
    print(f"  Canary  : {CYAN}{CANARY}{NC}")
    print(f"  Timeout : {CYAN}{TIMEOUT}s{NC}")
    print(f"  Tests   : {CYAN}{len(TESTS)}{NC}")

    if subprocess.run(["docker", "info"], capture_output=True).returncode != 0:
        print(f"\n  {RED}Error: Docker not available.{NC}")
        sys.exit(1)

    results = []
    passed = failed = 0

    for name, vuln_dir, poc_script, has_input in TESTS:
        ok, reason = run_test(name, vuln_dir, poc_script, has_input)
        if ok:
            passed += 1
            results.append(f"{GREEN}PASS{NC}  {name}")
        else:
            failed += 1
            results.append(f"{RED}FAIL{NC}  {name} ({reason})")

    print()
    print(f"{BOLD}╔══════════════════════════════════════════════════════════════╗{NC}")
    print(f"{BOLD}║                       Test Summary                           ║{NC}")
    print(f"{BOLD}╚══════════════════════════════════════════════════════════════╝{NC}")
    print()
    for r in results:
        print(f"  {r}")
    print()
    print(f"  Total  : {BOLD}{len(TESTS)}{NC}")
    print(f"  Passed : {GREEN}{passed}{NC}")
    print(f"  Failed : {RED}{failed}{NC}")
    print()
    if failed == 0:
        print(f"  {GREEN}{BOLD}All tests passed.{NC}")
    else:
        print(f"  {RED}{BOLD}Some tests failed.{NC}")
    sys.exit(0 if failed == 0 else 1)


if __name__ == "__main__":
    main()
