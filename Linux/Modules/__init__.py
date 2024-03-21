import glob
from os.path import basename, dirname, isfile

def __docs_modes():
    mod_pass = glob.glob(dirname(__file__) + "/*.py")
    modes = [
        basename(f)[:-3]
        for f in mod_pass
        if isfile(f) and f.endswith(".py") and not f.endswith("__init__.py")
    ]
    return modes

ALL_MODULES = sorted(__docs_modes())
__all__ = ALL_MODULES + ["ALL_MODULES"]
