import random
from player.player_ai import PlayerAI

class PlayerAIRandom(PlayerAI):
  def __init__(self, id):
    super().__init__(id)

  def algo_init(self):
    self.chosen_move = None
  
  def algo_iter(self, game):
    board = random.choice(game.global_board.get_active_boards())
    cell_index = random.choice(board.get_legal_moves())
    (row, col) = board.get_row_col(cell_index)

    self.chosen_move = {
      "board": board,
      "row": row,
      "col": col
    }
