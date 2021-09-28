from player.player_type import PlayerType
from player.player import Player

class PlayerHuman(Player):
  def __init__(self, id):
    super().__init__(id)
  
  def get_type(self):
    return PlayerType.Human
