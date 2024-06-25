from agents.storyteller import StoryTeller
from agents.player_interactor import PlayerInteractor

if __name__ == "__main__":
    storyteller = StoryTeller()
    player_interactor = PlayerInteractor()
    print(storyteller.tell_story())
    print(player_interactor.interact())
