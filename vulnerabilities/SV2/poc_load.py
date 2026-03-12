from skops.io import load, get_untrusted_types

unknown_types = get_untrusted_types(file="model.skops")
print("Unknown types", unknown_types)
input("Press enter to load the model...")
loaded = load("model.skops", trusted=unknown_types)