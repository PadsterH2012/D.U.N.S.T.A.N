from flask import Blueprint, jsonify

api = Blueprint('api', __name__)

@api.route('/api/characters', methods=['GET'])
def get_characters():
    # Example character data
    characters = [
        {"name": "Character 1"},
        {"name": "Character 2"},
        {"name": "Character 3"}
    ]
    return jsonify(characters)

@api.route('/api/quests', methods=['GET'])
def get_quests():
    # Example quest data
    quests = [
        {"title": "Quest 1"},
        {"title": "Quest 2"},
        {"title": "Quest 3"}
    ]
    return jsonify(quests)
