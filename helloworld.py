
import pygame 
from pygame.locals import *

from sys import exit

BACKGROUND_IMAGE = "./background/Screenshot 2026-05-10 185200.png"

pygame.init()

SCREEN = pygame.display.set_mode((640,480),0,32)

pygame.display.set_caption('Panda-Craps')

background = pygame.image.load(BACKGROUND_IMAGE).convert()

while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            exit()
    
    SCREEN.blit(background, (0,0))
    pygame.display.update()