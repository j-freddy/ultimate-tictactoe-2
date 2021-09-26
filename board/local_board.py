from cell.cell import Cell
from cell.cell_value import CellValue
from board.board import Board

# LocalBoard extends the interface of Cell

class LocalBoard(Board):
  def __init__(self):
    super().__init__()
    self.cells = [Cell(CellValue.Empty) for i in range(0, self.num_cells)]
    self.set_cell(0, 1, CellValue.O)
    self.set_cell(1, 1, CellValue.O)
    self.set_cell(2, 0, CellValue.X)
  
  def get_value(self):
    return self.get_winner()
  
  def set_cell(self, row, col, value):
    self.cells[self.get_cell_index(row, col)] = Cell(value)
