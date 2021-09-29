from board.global_board import GlobalBoard
from cell.cell_value import CellValue
from player.player_human import PlayerHuman
from player.player_ai_random import PlayerAIRandom

class Game:
  def __init__(self):
    self.global_board = GlobalBoard()
    self.player_x = PlayerHuman(CellValue.X)
    self.player_o = PlayerAIRandom(CellValue.O)
    self.current_player = self.player_x

  def get_result(self):
    return self.global_board.winner

  def in_progress(self):
    return self.global_board.winner == None

  def switch_players(self):
    self.current_player = (self.player_x
      if self.current_player == self.player_o
      else self.player_o)
  
  def make_move(self, board, row, col):
    valid_move = self.current_player.make_move(board, row, col)
    
    if valid_move:
      # Update status of prev local board
      board.update_winner()
      # Update status of global board
      self.global_board.update_winner()

      # Check if game is over
      if not self.in_progress():
        self.global_board.set_boards_inactive()
        return True

      # Update active boards
      self.global_board.update_active_boards((row, col))
      # Switch players
      self.switch_players()
    
    return valid_move
  
  def make_move_with_index(self, board, index):
    (row, col) = board.get_row_col(index)
    return self.make_move(board, row, col)
  
  # Returns whether move has been made
  def handle_ai_iter(self):
    if not self.current_player.is_ai():
      return

    ai = self.current_player

    # Initialises the AI if required (AI must be initialised per move)
    if ai.requires_init:
      ai.algo_init()

    # Perform 1 iteration
    ai.algo_iter(self)

    # Handle make move
    if ai.chosen_move == None:
      return False
    else:
      m = ai.chosen_move
      valid_move = self.make_move_with_index(m["board"], m["index"])
      # Prepare for next move
      ai.requires_init = True

      if not valid_move:
        print("AI made an invalid move")

      return True
