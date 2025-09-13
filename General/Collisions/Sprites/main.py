import pygame
from sys import exit
from obj import *

pygame.init()
screen = pygame.display.set_mode((800,650))
pygame.display.set_caption("Sprite Collisions")
clock = pygame.time.Clock()



while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()


    pygame.display.update()
    clock.tick(60)
