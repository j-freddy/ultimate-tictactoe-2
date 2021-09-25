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

### GUI

def draw_cell(cell, dim, x, y):
  img = images["o"] if cell.get_value() == CellValue.O else images["x"]
  img_scaled = pygame.transform.smoothscale(img, (dim, dim))
  screen.blit(img_scaled, (x, y))

def draw_local_board(board, board_dim, x, y):
  # Draw frame
  d = board_dim
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
        row * cell_dim + x,
        col * cell_dim + y
      )

def draw_global_board(board):
  global_board = board
  cell_dim = int(SCREEN_DIM / global_board.num_rows)

  for (i, local_board) in enumerate(global_board.cells):
    row = math.floor(i / global_board.num_cols)
    col = i % global_board.num_cols

    draw_local_board(
      local_board,
      cell_dim,
      row * cell_dim,
      col * cell_dim
    )

def draw(game):
  draw_global_board(game.global_board)

# Create game
game = Game()

screen.fill((255, 255, 255))
draw(game)
pygame.display.flip()

### Main loop

while True:
  clock.tick(60)

  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      sys.exit()

  # screen.fill((255, 255, 255))
  # draw(game)
  # pygame.display.flip()
