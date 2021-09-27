from cell.cell import Cell
from cell.cell_value import CellValue
from board.board import Board

# LocalBoard extends the interface of Cell

class LocalBoard(Board):
  def __init__(self):
    super().__init__()
    self.cells = [Cell(CellValue.Empty) for i in range(0, self.num_cells)]
    # Whether the board has a winner or is filled
    self.finalised = False
    self.active = False
  
  def get_value(self):
    return self.winner if self.winner != None else CellValue.Empty
  
  def set_cell(self, row, col, value):
    self.cells[self.get_cell_index(row, col)] = Cell(value)
  
  def update_status(self):
    if self.check_win(CellValue.X):
      self.winner = CellValue.X
      self.finalised = True
      return
    if self.check_win(CellValue.O):
      self.winner = CellValue.O
      self.finalised = True
      return
    # Draw
    if self.check_filled():
      self.winner = CellValue.Empty
      self.finalised = True
