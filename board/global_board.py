from board.board import Board
from board.local_board import LocalBoard

class GlobalBoard(Board):
  def __init__(self):
    super().__init__()
    self.cells = [LocalBoard() for i in range(0, self.num_cells)]
    self.set_boards_active()
  
  def set_boards_active(self):
    for board in self.cells:
      if not board.finalised:
        board.active = True
  
  def set_boards_inactive(self):
    for board in self.cells:
      board.active = False
