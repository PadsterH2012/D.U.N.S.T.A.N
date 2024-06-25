from api import app

@app.route('/api/characters')
def get_characters():
    return "This will return a list of characters."

@app.route('/api/quests')
def get_quests():
    return "This will return a list of quests."
