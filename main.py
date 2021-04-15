import pygame
from pygame.locals import *

class Game:
  def __init__(self):
    pygame.init()
    self.snake = Snake()
    self.snake.draw()

  def run(self):
    surface = pygame.display.set_mode((1000, 500))
    running = True

    while running:
      for event in pygame.event.get():
        if event.type == KEYDOWN:
          if event.key == K_ESCAPE:
            running = False

          if event.key == K_UP:
            block_y = block_y - 10
          

          if event.key == K_DOWN:
            block_y = block_y + 10
          

          if event.key == K_LEFT:
            block_x = block_x - 10
          

          if event.key == K_RIGHT:
            block_x += 10
          
        elif event.type == QUIT:
          running = False


class Snake:
  def __init__(self, parent_screen):
    self.parent_screen = parent_screen
    self.block = pygame.image.load("resources/block.jpg").convert()
    self.x = 100
    self.y = 100

  def draw(self):
    self.parent_screen.fill((73, 179, 101))
    self.parent_screen.blit(self.block, (self.x, self.y))
    pygame.display.flip()


if __name__ == "__main__":
  game = Game()
  game.run()
