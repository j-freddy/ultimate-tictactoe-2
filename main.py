import sys, pygame

pygame.init()

screen = pygame.display.set_mode((600, 600))
clock = pygame.time.Clock()

while True:
  clock.tick(60)

  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      sys.exit()

  screen.fill((255, 255, 255))
  pygame.display.flip()