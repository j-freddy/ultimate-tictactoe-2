from board.board import Board
from board.local_board import LocalBoard

class GlobalBoard(Board):
  def __init__(self):
    super().__init__()
    self.cells = [LocalBoard() for i in range(0, self.get_num_cells())]
    self.set_boards_active()
  
  def get_active_boards(self):
    return list(filter(lambda board: board.active, self.cells))
  
  def set_boards_active(self):
    for board in self.cells:
      if not board.finalised:
        board.active = True
  
  def set_boards_inactive(self):
    for board in self.cells:
      board.active = False
  
  def update_active_boards(self, last_move):
    (row, col) = last_move

    self.set_boards_inactive()

    next_board = self.get_cell(row, col)
    if next_board.finalised:
      self.set_boards_active()
    else:
      self.get_cell(row, col).active = True
