import keras


## Malicious Lambda Function
f = lambda x: (
    exec("import os; os.system('sh')"),
    x,
)

model = keras.Sequential()
model.add(keras.layers.Input(shape=(1,)))
model.add(keras.layers.Lambda(f))
model.compile()

model.save('baseline_malicious_lambda.keras')
model.save('baseline_malicious_lambda.h5')

## Non-Malicious Lambda Function
f = lambda x: (
    x,
)

model = keras.Sequential()
model.add(keras.layers.Input(shape=(1,)))
model.add(keras.layers.Lambda(f))
model.compile()

model.save('baseline_non_malicious_lambda.keras')
model.save('baseline_non_malicious_lambda.h5')

## No Lambda Function

model = keras.Sequential()
model.add(keras.layers.Input(shape=(1,)))
model.compile()

model.save('baseline_no_lambda.keras')
model.save('baseline_no_lambda.h5')