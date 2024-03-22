async def cosc_Push():
    from glob import glob
    from os.path import basename, dirname, isfile

    modas = glob(dirname(__file__) + "/*.py")
    apugs = [
        basename(f)[:-3]
        for so in modas
        if isfile(f) and so.endswith(".py") and not so.endswith("__init__.py")
    ]
    return sorted(apugs)
