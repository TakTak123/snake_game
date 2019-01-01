import sys 
import pygame
from pygame.locals import *
from random import randint

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
        self.x = [10, 9, 8]
        self.y = [10, 10, 10]
        self.length = 3
        self.speed = 1
        self.direction = RIGHT # 初期移動方向は右
        self.feed_count = 0 # 食べた回数

    def move(self): #x,yの後ろを吐き出して，先頭に座標を追加することで移動
        self.x.pop() 
        self.y.pop()
        
        if (self.direction == UP):
            # self.y -= 1
            self.x.insert(0, self.x[0])
            self.y.insert(0, self.y[0]-1)
        elif (self.direction == RIGHT):
            # self.x += 1
            self.x.insert(0, self.x[0]+1)
            self.y.insert(0, self.y[0])
        elif (self.direction == DOWN):
            # self.y += 1
            self.x.insert(0, self.x[0])
            self.y.insert(0, self.y[0]+1)
        else:
            # self.x -= 1
            self.x.insert(0, self.x[0]-1)
            self.y.insert(0, self.y[0])

    def grow(self): # とりあえず進行方向と逆向きに成長，けど壁に埋まる可能性
        if (self.direction == UP):
            self.x.append(self.x[-1])
            self.y.append(self.y[-1] - 1)
        elif (self.direction == RIGHT):
            self.x.append(self.x[-1] - 1)
            self.y.append(self.y[-1])
        elif (self.direction == DOWN):
            self.x.append(self.x[-1])
            self.y.append(self.y[-1] + 1)
        else:
            self.x.append(self.x[-1] + 1)
            self.y.append(self.y[-1])

        self.length += 1
    def draw(self, screen):
        for i in range(self.length):
            rect = pygame.Rect(20+BLOCK_SIZE*self.x[i], 20+BLOCK_SIZE*self.y[i], BLOCK_SIZE, BLOCK_SIZE)
            pygame.draw.rect(screen, (80, 200, 120), rect)

class Feed:
    def __init__(self, player):
        self.create_feed(player)

    def create_feed(self, player):
        self.x = randint(2, COLUMN_COUNT-3)
        self.y = randint(2, ROW_COUNT-3)
        while ((self.x == player.x) and (self.y == player.y)):
            self.create_feed(player)
    
    def draw(self, screen): 
        rect = pygame.Rect(20+BLOCK_SIZE*self.x, 20+BLOCK_SIZE*self.y, BLOCK_SIZE, BLOCK_SIZE)
        pygame.draw.rect(screen, (200, 80, 120), rect)

class ScoreBoard():
    def __init__(self):
        self.font = pygame.font.SysFont(None, 20)
        self.score = 0

    def draw(self, screen):
        score_img = self.font.render(str(self.score), True, (200, 200, 200))
        screen.blit(score_img, (600, 100))


class App:
    screen = pygame.display.set_mode((WIN_WIDTH, WIN_HEIGHT))

    def __init__(self):
        pygame.init()
        pygame.display.set_caption('Snake Game')
        self.player = Player()
        self.feed = Feed(self.player)
        self.score_board = ScoreBoard()
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
                    self.player.draw(self.screen) 
                    self.feed.draw(self.screen) 
                    self.score_board.draw(self.screen)

                if event.type == QUIT:
                    pygame.quit()
                    sys.exit
                pygame.display.update()
            
            timer_count += 1
            if (timer_count == 60000/self.player.speed): # playerの移動
                self.player.move()
                if (self.player.x[0] == self.feed.x and self.player.y[0] == self.feed.y):
                    self.feed.create_feed(self.player)
                    self.player.feed_count += 1
                    self.score_board.score += 10
    
                    if (self.player.feed_count % 3 == 0):
                        self.player.grow()
                        print(self.player.x)
                        print(self.player.y)
                        print('\n')
                self.draw_window()
                self.player.draw(self.screen) 
                self.feed.draw(self.screen)
                self.score_board.draw(self.screen)
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


if __name__ == '__main__':
    app = App()