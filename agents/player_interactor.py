# agents/player_interactor.py
def get_player_action(action):
    if action.lower() == "look around":
        return "You see trees all around. It's dark and quiet."
    else:
        return "Action not recognized."