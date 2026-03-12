import keras

keras.saving.load_model('poc.keras')

# It works with any parameter
# keras.saving.load_model('poc.keras', custom_objects={})
# keras.saving.load_model('poc.keras', custom_objects={}, safe_mode=True)
# keras.saving.load_model('poc.keras', custom_objects={}, safe_mode=False)
# keras.saving.load_model('poc.keras', custom_objects={}, safe_mode=True, compile=True)
# keras.saving.load_model('poc.keras', custom_objects={}, safe_mode=True, compile=False)