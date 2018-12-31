import sys 
import pygame
from pygame.locals import *

BLOCK_SIZE = 16
ROW_COUNT = 20
COLUMN_COUNT = 30
AREA_WIDTH = BLOCK_SIZE * COLUMN_COUNT
AREA_HEIGHT = BLOCK_SIZE * ROW_COUNT
WIN_WIDTH = AREA_WIDTH + 200
WIN_HEIGHT = AREA_HEIGHT + 200


class App:
    screen = pygame.display.set_mode((WIN_WIDTH, WIN_HEIGHT))

    def __init__(self):
        pygame.init()
        pygame.display.set_caption('Snake Game')
        self.init_window()
        pygame.display.update()
        while True:
            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()
                    sys.exit
                pygame.display.update()

    def init_window(self):
        self.screen.fill((30, 30, 30)) # 背景の設定
        # grid作成
        for y in range(ROW_COUNT): 
            for x in range(COLUMN_COUNT):
                rect = pygame.Rect(20+BLOCK_SIZE*x, 20+BLOCK_SIZE*y, BLOCK_SIZE, BLOCK_SIZE)
                pygame.draw.rect(self.screen, (150, 150, 150), rect, 1)

        # wall作成
        for x in range(COLUMN_COUNT):
            rect = pygame.Rect(20+BLOCK_SIZE*x, 20, BLOCK_SIZE, BLOCK_SIZE)
            pygame.draw.rect(self.screen, (200, 200, 200), rect)
            rect = pygame.Rect(20+BLOCK_SIZE*x, 20+AREA_HEIGHT-BLOCK_SIZE, BLOCK_SIZE, BLOCK_SIZE)
            pygame.draw.rect(self.screen, (200, 200, 200), rect)
        for y in range(ROW_COUNT):
            rect = pygame.Rect(20, 20+BLOCK_SIZE*y, BLOCK_SIZE, BLOCK_SIZE)
            pygame.draw.rect(self.screen, (200, 200, 200), rect)
            rect = pygame.Rect(20+AREA_WIDTH-BLOCK_SIZE, 20+BLOCK_SIZE*y, BLOCK_SIZE, BLOCK_SIZE)
            pygame.draw.rect(self.screen, (200, 200, 200), rect)
            
if __name__ == '__main__':
    app = App()