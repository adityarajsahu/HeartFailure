from sklearn.pipeline import Pipeline
from HeartFailure.config import config
import HeartFailure.processing.preprocessing as pp
from sklearn.preprocessing import MinMaxScaler
from sklearn.linear_model import LogisticRegression
import numpy as np

classification_pipeline = Pipeline(
    [
        ("MeanImputation", pp.MeanImputer(variables=config.NUM_FEATURES)),
        ("ModeImputer", pp.ModeImputer(variables=config.CAT_FEATURES)),
        ("LabelEncoder", pp.CustomLabelEncoder(variables=config.CAT_FEATURES)),
        ("MinMaxScaler", MinMaxScaler()),
        ("LogisticClassifier", LogisticRegression(random_state=0))
    ]
)