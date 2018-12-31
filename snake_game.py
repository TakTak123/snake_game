import sys 
import pygame
from pygame.locals import *

BLOCK_SIZE = 20
HEIGHT = BLOCK_SIZE * 20
WIDTH = BLOCK_SIZE * 30

class App:
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Snake Game")

    def __init__(self):
        pygame.init()
        self.init_window()
        while True:
            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()
                    sys.exit
                pygame.display.update()

    def init_window(self):
        self.screen.fill((0, 0, 0))
        for y in range(HEIGHT):
            for x in range(WIDTH):
                rect = pygame.Rect(x*BLOCK_SIZE, y*BLOCK_SIZE, BLOCK_SIZE, BLOCK_SIZE)
                pygame.draw.rect(self.screen, (180, 60, 60), rect, 1)

if __name__ == "__main__":
    app = App()