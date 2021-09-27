import sys, os, math, pygame
from cell.cell_value import CellValue
from game import Game

pygame.init()

SCREEN_WIDTH = 540
SCREEN_HEIGHT = 540
SCREEN_DIM = min(SCREEN_WIDTH, SCREEN_HEIGHT)
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
clock = pygame.time.Clock()

def load_image(path):
  return pygame.image.load(path).convert_alpha()

# Methods in a dictionary are called once
# The return result is stored
images = {
  "o"          : load_image(os.path.join("img", "o.png")),
  "x"          : load_image(os.path.join("img", "x.png")),
  "board-frame": load_image(os.path.join("img", "board-frame.png"))
}

gui_data = {
  "highlight_colour": (255, 255, 0)
}

### GUI

def draw_cell(cell, dim, x, y):
  img = images["o"] if cell.get_value() == CellValue.O else images["x"]
  img_scaled = pygame.transform.smoothscale(img, (dim, dim))
  screen.blit(img_scaled, (x, y))

def draw_local_board(board, board_dim, x, y):
  d = board_dim

  # Highlight board if active
  if board.active:
    pygame.draw.rect(screen, gui_data["highlight_colour"], (x, y, d, d))

  # Draw frame
  img_frame = pygame.transform.smoothscale(images["board-frame"], (d, d))
  screen.blit(img_frame, (x, y))

  # Draw cells
  cell_dim = int(board_dim / board.num_rows)

  for (i, cell) in enumerate(board.cells):
    if cell.get_value() != CellValue.Empty:
      row = math.floor(i / board.num_cols)
      col = i % board.num_cols

      draw_cell(
        cell,
        cell_dim,
        col * cell_dim + x,
        row * cell_dim + y
      )
  
  # Draw winner
  if board.get_value() != CellValue.Empty:
    img = images["o"] if board.get_value() == CellValue.O else images["x"]
    img_scaled = pygame.transform.smoothscale(img, (d, d))
    screen.blit(img_scaled, (x, y))

def draw_global_board(board):
  global_board = board
  cell_dim = int(SCREEN_DIM / global_board.num_rows)

  for (i, local_board) in enumerate(global_board.cells):
    row = math.floor(i / global_board.num_cols)
    col = i % global_board.num_cols

    draw_local_board(
      local_board,
      cell_dim,
      col * cell_dim,
      row * cell_dim
    )

def draw(game):
  screen.fill((255, 255, 255))

  # Draw winner
  if not game.in_progress():
    screen.fill((0, 255, 0))

  draw_global_board(game.global_board)

  pygame.display.flip()

def on_click(board):
  # Get local board clicked
  global_cell_dim = int(SCREEN_DIM / board.num_rows)
  (mouse_x, mouse_y) = pygame.mouse.get_pos()
  row = math.floor(mouse_y / global_cell_dim)
  col = math.floor(mouse_x / global_cell_dim)
  local_board = board.get_cell(row, col)

  # Get cell clicked on local board
  local_cell_dim = int(global_cell_dim / local_board.num_rows)
  local_x = mouse_x % global_cell_dim
  local_y = mouse_y % global_cell_dim
  row = math.floor(local_y / local_cell_dim)
  col = math.floor(local_x / local_cell_dim)
  
  # Update cell
  game.make_move(local_board, row, col)

# Create game
game = Game()
draw(game)

### Main loop
while True:
  clock.tick(60)

  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      sys.exit()
    if event.type == pygame.MOUSEBUTTONDOWN:
      if game.in_progress():
        on_click(game.global_board)
        draw(game)
