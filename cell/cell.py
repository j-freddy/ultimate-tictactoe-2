from cell.cell_value import CellValue

class Cell:
  def __init__(self):
    self.value = CellValue.O
  
  def get_value(self):
    return self.value
