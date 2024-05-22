from sklearn.pipeline import Pipeline
from sklearn.preprocessing import MinMaxScaler
from sklearn.linear_model import LogisticRegression
import numpy as np
from pathlib import Path
import os
import sys

PACKAGE_ROOT = Path(os.path.abspath(os.path.dirname(__file__))).parent
sys.path.append(str(PACKAGE_ROOT))

from HeartFailure.config import config
import HeartFailure.processing.preprocessing as pp

classification_pipeline = Pipeline(
    [
        ("MeanImputation", pp.MeanImputer(variables=config.NUM_FEATURES)),
        ("ModeImputer", pp.ModeImputer(variables=config.CAT_FEATURES)),
        ("LabelEncoder", pp.CustomLabelEncoder(variables=config.CAT_FEATURES)),
        ("MinMaxScaler", MinMaxScaler()),
        ("LogisticClassifier", LogisticRegression(random_state=0))
    ]
)