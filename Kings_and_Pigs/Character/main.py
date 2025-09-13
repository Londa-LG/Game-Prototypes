import pygame 
from sys import exit

pygame.init()
screen = pygame.display.set_mode((800,400))
pygame.display.set_caption("Character prototypes")
clock = pygame.tick.Clock()

while True:
    clock.tick(60)

    for event in pygame.event.get()
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

    pygame.display.update()
