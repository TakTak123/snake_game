import sys 
import pygame
from pygame.locals import *

BLOCK_SIZE = 20
HEIGHT = BLOCK_SIZE * 20
WIDTH = BLOCK_SIZE * 30

pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Snake Game")

def main():
    screen.fill((0, 0, 0))
    for y in range(HEIGHT):
        for x in range(WIDTH):
            rect = pygame.Rect(x*BLOCK_SIZE, y*BLOCK_SIZE, BLOCK_SIZE, BLOCK_SIZE)
            pygame.draw.rect(screen, (120, 60, 60), rect, 1)
            
    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit
        pygame.display.update()

if __name__ == "__main__":
    main()