import keras

keras.saving.load_model('poc.h5')

# It works with any parameter
# keras.saving.load_model('poc.h5', custom_objects={})
# keras.saving.load_model('poc.h5', custom_objects={}, safe_mode=True)
# keras.saving.load_model('poc.h5', custom_objects={}, safe_mode=False)
# keras.saving.load_model('poc.h5', custom_objects={}, safe_mode=True, compile=True)
# keras.saving.load_model('poc.h5', custom_objects={}, safe_mode=True, compile=False)