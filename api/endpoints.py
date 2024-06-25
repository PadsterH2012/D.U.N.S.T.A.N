# api/endpoints.py
from flask import Blueprint, request, jsonify
from agents.storyteller import get_story
from agents.player_interactor import get_player_action

api_blueprint = Blueprint('api', __name__)

@api_blueprint.route('/get_story', methods=['GET'])
def story():
    return jsonify({"story": get_story()})

@api_blueprint.route('/player_action', methods=['POST'])
def player_action():
    action = request.json.get('action')
    result = get_player_action(action)
    return jsonify({"result": result})