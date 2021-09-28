from cell.cell_value import CellValue
from board.local_board import LocalBoard

board = LocalBoard()
board.set_cell(0, 0, CellValue.O)

print(board.get_legal_moves())
