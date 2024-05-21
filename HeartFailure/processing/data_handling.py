import os
import pandas as pd
import joblib
from HeartFailure.config import config

# Load the dataset
def load_dataset(file_name):
    filepath = os.path.join(config.DATAPATH, file_name)
    _data = pd.read_csv(filepath)
    return _data

# Serialization
def save_pipeline(pipeline_to_save):
    save_path = os.path.join(config.SAVED_MODEL, config.MODEL_NAME)
    joblib.dump(pipeline_to_save, save_path)
    print("Pipeline Saved: {}".format(save_path))

# Deserialization
def load_pipeline():
    load_path = os.path.join(config.SAVED_MODEL, config.MODEL_NAME)
    loaded_model = joblib.load(load_path)
    print("Pipeline Loaded")
    return loaded_model