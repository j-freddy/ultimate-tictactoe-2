from cell.cell_value import CellValue
from board.board import Board
from board.local_board import LocalBoard

class GlobalBoard(Board):
  def __init__(self):
    super().__init__()
    self.cells = [LocalBoard() for i in range(0, self.get_num_cells())]
    self.set_boards_active()
  
  def finalised(self):
    return not list(filter(lambda board: not board.finalised, self.cells))
  
  def get_active_boards(self):
    return list(filter(lambda board: board.active, self.cells))
  
  def get_active_boards_with_index(self):
    boards = []

    for (i, board) in enumerate(self.cells):
      if board.active:
        boards.append((board, i))
    
    return boards
  
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
    
  def update_winner(self):
    if self.check_win(CellValue.X):
      self.winner = CellValue.X
      return
    if self.check_win(CellValue.O):
      self.winner = CellValue.O
      return
    if self.finalised():
      self.winner = CellValue.Empty

  def clone(self):
    cloned_board = GlobalBoard()
    cloned_board.cells = [cell.clone() for cell in self.cells]
    cloned_board.winner = self.winner

    return cloned_board
