from player.player_type import PlayerType
from player.player import Player

### AI Interface

# ai.algo_init() sets up the environment to run the algorithm
# ai.algo_iter() performs 1 iteration of the algorithm
# Once the AI has chosen its move, the move is stored in ai.chosen_move

class PlayerAI(Player):
  def __init__(self, id):
    super().__init__(id)
    self.requires_init = True
    # Move is represented as { board, index }
    self.chosen_move = None
  
  def get_type(self):
    return PlayerType.AI

  def algo_init(self):
    pass
  
  def algo_iter(self):
    pass
