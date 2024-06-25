from agents.storyteller import StoryTeller
from agents.player_interactor import PlayerInteractor

if __name__ == "__main__":
    storyteller = StoryTeller()
    player_interactor = PlayerInteractor()
    scene = "a dark forest"  # Provide a sample scene
    print(storyteller.tell_story(scene))
    print(player_interactor.interact("explore the area"))
