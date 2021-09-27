from cell.cell_value import CellValue

class Board:
  def __init__(self):
    self.num_cells = 9
    self.num_rows = 3
    self.num_cols = 3
    self.cells = []
    self.winning_cases = [
      [0, 1, 2], [3, 4, 5], [6, 7, 8],
      [0, 3, 6], [1, 4, 7], [2, 5, 8],
      [0, 4, 8], [2, 4, 6]
    ]
    self.winner = None

  def get_cell_index(self, row, col):
    return row * self.num_cols + col
  
  def get_cell(self, row, col):
    return self.cells[self.get_cell_index(row, col)]

  def check_filled(self):
    for cell in self.cells:
      if cell.get_value() == CellValue.Empty:
        return False
    
    return True

  def check_win(self, cell_value):
    cell_values = [cell.get_value() for cell in self.cells]

    for indices in self.winning_cases:
      matches = [cell_values[i] == cell_value for i in indices]
      if set(matches) == {True}:
        return True
    
    return False
  
  def print(self):
    string = ""

    index = 0
    for i in range(0, self.num_rows):
      for j in range(0, self.num_cols):
        string += self.cells[index].get_value().value + " "
        index += 1

      string += "\n"

    print(string)
