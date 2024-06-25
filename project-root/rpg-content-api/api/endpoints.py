from api import app

@app.route('/api/characters', methods=['GET'])
def get_characters():
    return "This will return a list of characters."

@app.route('/api/quests', methods=['GET'])
def get_quests():
    return "This will return a list of quests."
