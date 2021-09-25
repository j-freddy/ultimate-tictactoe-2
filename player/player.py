class Player:
  def __init__(self, id):
    self.id = id
  
  def make_move(self, board, row, col):
    board.set_cell(row, col, self.id)
