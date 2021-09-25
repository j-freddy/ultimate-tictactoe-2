from cell.cell_value import CellValue

class Board:
  def __init__(self):
    self.num_cells = 9
    self.num_rows = 3
    self.num_cols = 3
    self.cells = []

  def get_winner(self):
    return CellValue.X
  
  def print(self):
    string = ""

    index = 0
    for i in range(0, self.num_rows):
      for j in range(0, self.num_cols):
        string += self.cells[index].get_value().value + " "
        index += 1

      string += "\n"

    print(string)
