from cell.cell_value import CellValue
from cell.cell import Cell
from board.board import Board

# LocalBoard extends the interface of Cell

class LocalBoard(Board):
  def __init__(self):
    super().__init__()
    self.cells = [Cell() for i in range(0, 9)]
    self.cells[2].value = CellValue.X
    self.cells[4].value = CellValue.Empty
  
  def get_value(self):
    return self.get_winner()
