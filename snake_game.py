import sys 
import pygame
from pygame.locals import *

BLOCK_SIZE = 20
ROW_COUNT = 20
COLUMN_COUNT = 30
HEIGHT = BLOCK_SIZE * ROW_COUNT
WIDTH = BLOCK_SIZE * COLUMN_COUNT

class App:
    screen = pygame.display.set_mode((WIDTH+300, HEIGHT+300))
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
        self.screen.fill((0, 0, 0)) # 背景を黒に
        for y in range(ROW_COUNT): # グリッドの作成
            for x in range(COLUMN_COUNT):
                rect = pygame.Rect(20+x*BLOCK_SIZE, 20+y*BLOCK_SIZE, BLOCK_SIZE, BLOCK_SIZE)
                pygame.draw.rect(self.screen, (200, 200, 200), rect, 0.5)

if __name__ == "__main__":
    app = App()