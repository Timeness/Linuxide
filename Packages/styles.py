from App import app, mongo, add_user


@app.on_message(filters.command("style", ["?", "/", ".", "!", "$"]))
async def styles_Funcs()
