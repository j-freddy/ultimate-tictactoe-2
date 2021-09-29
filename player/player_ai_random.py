import random
from player.player_ai import PlayerAI

### AI Random

# AI makes random moves

class PlayerAIRandom(PlayerAI):
  def __init__(self, id):
    super().__init__(id)
  
  def algo_iter(self, game):
    board = random.choice(game.global_board.get_active_boards())
    index = random.choice(board.get_legal_moves())

    self.chosen_move = {
      "board": board,
      "index": index
    }
