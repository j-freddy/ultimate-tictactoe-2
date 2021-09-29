from cell.cell_value import CellValue
from player.player_ai import PlayerAI
import random

### AI Random Feedback

# AI makes random moves from current position until game over
# AI then updates the weighting/evaluation of the first move
# Process repeats n times
# AI chooses the move with the highest weighting

class PlayerAIRandomFeedback(PlayerAI):
  def __init__(self, id):
    super().__init__(id)
    self.iter_count = 0
    self.max_iterations = 60
    self.simulations_per_iter = 20
    self.move_weightings = []
  
  def get_best_move(self):
    return max(self.move_weightings, key=lambda m: m.weight())

  def algo_init(self, game):
    super().algo_init(game)

    self.iter_count = 0
    self.move_weightings = []

    for (board, i) in game.global_board.get_active_boards_with_index():
      for move_index in board.get_legal_moves():
        self.move_weightings.append(
          PlayerAIRandomFeedback.MoveData(i, move_index)
        )
  
  def algo_iter(self, game):
    self.iter_count += 1

    for i in range(0, 10):
      # Create clone of game
      game_clone = game.clone()
      # Choose a move in move data
      move = random.choice(self.move_weightings)
      # Make move on board
      local_board_clone = game_clone.global_board.cells[move.board_index]
      game_clone.make_move_with_index(local_board_clone, move.index)

      # Simulate game with random moves
      while game_clone.in_progress():
        if (game_clone.global_board.get_active_boards() == []):
          for board in game_clone.global_board.cells:
            board.print()

        board = random.choice(game_clone.global_board.get_active_boards())
        index = random.choice(board.get_legal_moves())

        game_clone.make_move_with_index(board, index)
      
      # Update result
      if game_clone.get_result() == self.id:
        move.raw_weight += 1
      elif game_clone.get_result() == CellValue.Empty:
        move.raw_weight += 0.5

      move.num_simulations += 1

    # Choose move when iteration limit reached
    if self.iter_count >= self.max_iterations:
      print("--- Summary ---")
      for m in self.move_weightings:
        m.print()
      print("---------------")
      
      best_move = self.get_best_move()
      self.chosen_move = {
        "board": game.global_board.cells[best_move.board_index],
        "index": best_move.index
      }
  
  class MoveData:
    def __init__(self, board_index, index):
      self.board_index = board_index
      self.index = index
      self.raw_weight = 0
      self.num_simulations = 0
    
    def weight(self):
      # Edge case: move hasn't been simulated
      if self.num_simulations == 0:
        return 0

      return self.raw_weight / self.num_simulations
    
    def print(self):
      string = "Move\n"
      string += "Board " + str(self.board_index)\
        + ", move " + str(self.index) + "\n"
      string += "Weight: " + str(round(self.weight(), 2))\
        + " (" + str(self.raw_weight) + "/"\
        + str(self.num_simulations) + ")" + "\n"

      print(string)
