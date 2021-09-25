from cell.cell_value import CellValue
from cell.cell_value import CellValue
from board.local_board import LocalBoard
from player.player import Player

class Game:
  def __init__(self):
    self.local_board = LocalBoard()
    self.player = Player(CellValue.X)
    self.player.make_move(self.local_board, 0, 2)
    self.player.make_move(self.local_board, 1, 2)
    self.player.make_move(self.local_board, 2, 0)
    self.player.make_move(self.local_board, 2, 1)
    self.local_board.print()

game = Game()
