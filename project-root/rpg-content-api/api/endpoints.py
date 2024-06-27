from flask import Blueprint, jsonify, request
from .models import db, Character, Quest

api = Blueprint('api', __name__)

@api.route('/api/characters', methods=['GET'])
def list_characters():
    characters = Character.query.all()
    return jsonify([char.to_dict() for char in characters])

@api.route('/api/quests', methods=['GET'])
def list_quests():
    quests = Quest.query.all()
    return jsonify([quest.to_dict() for quest in quests])
