from cell.cell import Cell
from board.board import Board

# LocalBoard extends the interface of Cell

class LocalBoard(Board):
  def __init__(self):
    super().__init__()
    self.cells = [Cell() for i in range(0, self.num_cells)]
  
  def get_value(self):
    return self.get_winner()
  
  def set_cell(self, row, col, value):
    self.cells[row*self.num_cols + col] = Cell(value)