import os
from HeartFailure.config import config

with open(os.path.join(config.PACKAGE_ROOT, "VERSION")) as file:
    __version__ = file.read().strip()