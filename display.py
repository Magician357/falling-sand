import sys

import pygame
from pygame.locals import *

from random import randint
from elements import grid

def Render_Text(string, pos, color=(255,255,255)):
    font = pygame.font.SysFont("arial",50)
    text = font.render(string, 1, pygame.Color(color))
    screen.blit(text, pos)

grid_width=100
grid_height=100

test=grid(grid_width,grid_height)

for _ in range(500):
    test[randint(0,grid_width-1),randint(0,grid_height-1)].color=(randint(0,255),randint(0,255),randint(0,255))

pygame.init()

fps = 120
clock = pygame.time.Clock()

width, height = grid_width*10,grid_height*10
screen = pygame.display.set_mode((width, height))

print(pygame.font.get_fonts())

# Game loop.
while True:
    screen.fill((0, 0, 0))
    
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
    
    # Update
    
    
    # Draw
    
    for y, row in enumerate(test.grid):
        for x, cell in enumerate(row):
            pygame.draw.rect(screen,cell.color,Rect((x*10,y*10),((x+1)*10,(y+1)*10)))
    
    clock.tick(fps)
    Render_Text(str(int(clock.get_fps())), (100,100))
    print(clock.get_fps())
    
    pygame.display.flip()
    
    