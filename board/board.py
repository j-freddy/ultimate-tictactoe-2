from cell.cell_value import CellValue

class Board:
  def __init__(self):
    self.cells = []

  def get_winner(self):
    return CellValue.X
  
  def print(self):
    string = ""

    for cell in self.cells:
      string += cell.get_value().value + " "

    print(string)
