import pandas as pd
import numpy as np
from pathlib import Path
import os
import sys

PACKAGE_ROOT = Path(os.path.abspath(os.path.dirname(__file__))).parent
sys.path.append(str(PACKAGE_ROOT))

from HeartFailure.config import config
from HeartFailure.processing.data_handling import load_dataset, save_pipeline
import HeartFailure.processing.preprocessing as pp
import HeartFailure.pipeline as pipe

def perform_training():
    train_data = load_dataset(config.TRAIN_FILE)
    train_y = train_data[config.TARGET]
    pipe.classification_pipeline.fit(train_data[config.FEATURES], train_y)
    save_pipeline(pipe.classification_pipeline)

if __name__ == "__main__":
    perform_training()