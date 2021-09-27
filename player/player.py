class Player:
  def __init__(self, id):
    self.id = id
  
  # Do not call directly, instead call game.make_move()
  def make_move(self, board, row, col):
    if not (board.active and board.get_cell(row, col).is_empty()):
      return False

    board.set_cell(row, col, self.id)
    return True
