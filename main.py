import sys, os, math, pygame
from cell.cell_value import CellValue
from game import Game

pygame.init()

SCREEN_WIDTH = 540
SCREEN_HEIGHT = 540
SCREEN_DIM = min(SCREEN_WIDTH, SCREEN_HEIGHT)
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
clock = pygame.time.Clock()

images = {
  "o": pygame.image.load(os.path.join("img", "o.png")).convert_alpha(),
  "x": pygame.image.load(os.path.join("img", "x.png")).convert_alpha()
}

### GUI functions

def draw(game):
  for (i, cell) in enumerate(game.local_board.cells):
    if cell.get_value() == CellValue.Empty:
      continue

    row = math.floor(i / game.local_board.num_cols)
    col = i % game.local_board.num_cols
    dim = int(SCREEN_DIM / 9)

    img = images["o"] if cell.get_value() == CellValue.O else images["x"]
    img_scaled = pygame.transform.smoothscale(img, (dim, dim))
    screen.blit(img_scaled, (dim * row, dim * col))

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
