import glob
from os.path import basename, dirname, isfile

def __acc_modes():
    mod_pass = glob.glob(dirname(__file__) + "/*.py")
    aoc_modes = [
        basename(f)[:-3]
        for so in mod_pass
        if isfile(so) and so.endswith(".py") and not so.endswith("__init__.py") and not so.endswith("cloneFunc.py") and not so.endswith("syncFunc.py")
    ]
    return aoc_modes


ALL_MODULES = sorted(__acc_modes())
__all__ = ALL_MODULES + ["ALL_MODULES"]
