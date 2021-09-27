from board.global_board import GlobalBoard
from cell.cell_value import CellValue
from cell.cell_value import CellValue
from player.player import Player

class Game:
  def __init__(self):
    self.global_board = GlobalBoard()
    self.player_x = Player(CellValue.X)
    self.player_o = Player(CellValue.O)
    self.current_player = self.player_x

  def switch_players(self):
    self.current_player = (self.player_x
      if self.current_player == self.player_o
      else self.player_o)
  
  def make_move(self, board, row, col):
    valid_move = self.current_player.make_move(board, row, col)
    
    if valid_move:
      self.global_board.set_boards_inactive()
      self.global_board.get_cell(row, col).active = True
      self.switch_players()
    
    return valid_move
