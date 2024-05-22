import pandas as pd
import numpy as np
import joblib
from pathlib import Path
import os
import sys

PACKAGE_ROOT = Path(os.path.abspath(os.path.dirname(__file__))).parent
sys.path.append(str(PACKAGE_ROOT))

from HeartFailure.config import config
from HeartFailure.processing.data_handling import load_pipeline, load_dataset

classification_pieline = load_pipeline()

# def generate_predictions(data_input):
#     data = pd.DataFrame(data_input)
#     pred = classification_pieline.predict(data[config.FEATURES])
#     result = { "Predictions": pred }
#     return result

def generate_predictions():
    test_data = load_dataset(config.TEST_FILE)
    pred = classification_pieline.predict(test_data[config.FEATURES])
    result = { "Predictions": pred }
    return result

if __name__ == "__main__":
    results = generate_predictions()
    print(results)