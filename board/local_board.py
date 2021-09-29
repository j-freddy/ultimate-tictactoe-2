from cell.cell import Cell
from cell.cell_value import CellValue
from board.board import Board

# LocalBoard extends the interface of Cell

class LocalBoard(Board):
  def __init__(self):
    super().__init__()
    self.cells = [Cell() for i in range(0, self.get_num_cells())]
    # Whether the board has a winner or is filled
    self.finalised = False
    self.active = False
  
  def get_value(self):
    return self.winner if self.winner != None else CellValue.Empty
  
  def set_cell(self, row, col, value):
    self.cells[self.get_cell_index(row, col)] = Cell(value)
  
  def check_filled(self):
    for cell in self.cells:
      if cell.get_value() == CellValue.Empty:
        return False
    
    return True
  
  # Returns a list of legal moves, represented as cell indices
  def get_legal_moves(self):
    moves = []

    for (i, cell) in enumerate(self.cells):
      if cell.is_empty():
        moves.append(i)
    
    return moves
  
  def update_winner(self):
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

  def clone(self):
    cloned_board = LocalBoard()
    cloned_board.cells = [cell.clone() for cell in self.cells]
    cloned_board.winner = self.winner
    cloned_board.finalised = self.finalised
    cloned_board.active = self.active

    return cloned_board
