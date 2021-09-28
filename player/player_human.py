from player.player import Player

class PlayerHuman(Player):
  def __init__(self, id):
    super().__init__(id)
  
  def interactable(self):
      return True
