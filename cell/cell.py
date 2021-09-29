from cell.cell_value import CellValue

# The point of this class is that Cell and LocalBoard share get_value()
# So the same check_win() method can be used for LocalBoard and GlobalBoard

class Cell:
  def __init__(self, value=CellValue.Empty):
    self.value = value
  
  def get_value(self):
    return self.value
  
  def is_empty(self):
    return self.value == CellValue.Empty

  def clone(self):
    return Cell(self.value)
