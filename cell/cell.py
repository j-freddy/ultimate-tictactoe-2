from cell.cell_value import CellValue

class Cell:
  def __init__(self, value=CellValue.Empty):
    self.value = value
  
  def get_value(self):
    return self.value
