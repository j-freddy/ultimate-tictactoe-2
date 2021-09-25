from board.board import Board
from board.local_board import LocalBoard

class GlobalBoard(Board):
  def __init__(self):
    super().__init__()
    self.cells = [LocalBoard() for i in range(0, self.num_cells)]
