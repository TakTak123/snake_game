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
UP = 0
RIGHT = 1
DOWN = 2
LEFT = 3

class Player:
    def __init__(self):
        self.x = 10
        self.y = 10
        self.speed = 1
        self.direction = RIGHT

    def move(self):
        if (self.direction == UP):
            self.y -= 1
        elif (self.direction == RIGHT):
            self.x += 1
        elif (self.direction == DOWN):
            self.y += 1
        else:
            self.x -= 1

class App:
    screen = pygame.display.set_mode((WIN_WIDTH, WIN_HEIGHT))
    # player = 0

    def __init__(self):
        pygame.init()
        pygame.display.set_caption('Snake Game')
        self.player = Player()
        self.draw_window()
        self.draw_player()
        pygame.display.update()

        timer_count = 0
        while True:
            for event in pygame.event.get():
                if event.type == KEYDOWN:
                    if event.key == K_RIGHT:
                        self.player.direction = RIGHT
                    if event.key == K_LEFT:
                        self.player.direction = LEFT
                    if event.key == K_UP:
                        self.player.direction = UP
                    if event.key == K_DOWN:
                        self.player.direction = DOWN
                    self.draw_window()
                    self.draw_player()  

                if event.type == QUIT:
                    pygame.quit()
                    sys.exit
                pygame.display.update()
            
            timer_count += 1
            if (timer_count == 60000/self.player.speed):
                self.player.move()
                self.draw_window()
                self.draw_player()
                pygame.display.update()
                timer_count = 0


    def draw_window(self):
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

    def draw_player(self):
        rect = pygame.Rect(20+BLOCK_SIZE*self.player.x, 20+BLOCK_SIZE*self.player.y, BLOCK_SIZE, BLOCK_SIZE)
        pygame.draw.rect(self.screen, (80, 200, 120), rect)       
            

 
if __name__ == '__main__':
    app = App()