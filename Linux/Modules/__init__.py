import glob
from os.path import basename, dirname, isfile

def __docs_modes():
    mod_pass = glob.glob(dirname(__file__) + "/*.py")
    modes = [
        basename(o)[:-3]
        for o in mod_pass
        if isfile(o) and o.endswith(".py") and not o.endswith("__init__.py") and not o.endswith("SysCore.py")
    ]
    return modes

ALL_MODULES = sorted(__docs_modes())
__all__ = ALL_MODULES + ["ALL_MODULES"]
