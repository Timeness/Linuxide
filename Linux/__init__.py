
    
class Pyro():
    Soumo = PyGram(
        name="PyroSoumo",
        api_id=Config.API_ID,
        api_hash=Config.API_HASH,
        bot_token=Config.BOT_TOKEN,
        plugins=dict(root="Packages"),
        workers=Config.SELF_WORKERS,
        in_memory=True
    )
App = Pyro.Soumo

class Hydro():
    Soumo = HyGram(
        name="HydroSoumo",
        api_id=Config.API_ID,
        api_hash=Config.API_HASH,
        bot_token=Config.BOT_TOKEN,
        plugins=dict(root="Packages"),
        workers=Config.SELF_WORKERS,
        in_memory=True
    )
Sakura = Hydro.Soumo
