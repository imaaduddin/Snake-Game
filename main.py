import pygame
from pygame.locals import *



if __name__ == "__main__":
  pygame.init()

  surface = pygame.display.set_mode((1000, 500))
  surface.fill((73, 179, 101))
  pygame.display.flip()
  
  running = True

  while running:
    for event in pygame.event.get():
      if event.type == KEYDOWN:
        pass
      elif event.type == QUIT:
        running = False