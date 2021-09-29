from cell.cell_value import CellValue
from board.local_board import LocalBoard
from board.global_board import GlobalBoard

board = GlobalBoard()
board.get_cell(0, 0).set_cell(2, 2, CellValue.X)

board_clone = board.clone()
board_clone.get_cell(0, 0).set_cell(2, 1, CellValue.X)

board.get_cell(0, 0).print()
board_clone.get_cell(0, 0).print()
