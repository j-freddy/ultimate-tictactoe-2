from board.global_board import GlobalBoard
from cell.cell_value import CellValue
from cell.cell_value import CellValue
from board.local_board import LocalBoard
from player.player import Player

class Game:
  def __init__(self):
    self.global_board = GlobalBoard()
    self.player_x = Player(CellValue.X)
    self.player_o = Player(CellValue.O)
