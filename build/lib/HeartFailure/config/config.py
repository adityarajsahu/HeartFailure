import pathlib
import os
import HeartFailure

PACKAGE_ROOT = pathlib.Path(HeartFailure.__file__).resolve().parent
DATAPATH = os.path.join(PACKAGE_ROOT, "datasets")

TRAIN_FILE = "train.csv"
TEST_FILE = "test.csv"

MODEL_NAME = "classification.pkl"
SAVED_MODEL = os.path.join(PACKAGE_ROOT, "trained_models")

TARGET = "HeartDisease"

FEATURES = ["Age", "Sex", "ChestPainType", "RestingBP", "Cholesterol", "FastingBS", "RestingECG", "MaxHR", "ExerciseAngina", "Oldpeak", "ST_Slope"]

CAT_FEATURES = ["Sex", "ChestPainType", "FastingBS", "RestingECG", "ExerciseAngina", "ST_Slope"]

NUM_FEATURES = ["Age", "RestingBP", "Cholesterol", "MaxHR", "Oldpeak"]
