import pygame 
from sys import exit
from characters import HumanKing

pygame.init()
screen = pygame.display.set_mode((800,400))
pygame.display.set_caption("Character prototypes")
clock = pygame.time.Clock()

player = HumanKing(screen,(400, 200))
bg = pygame.Surface((800,400))
bg.fill("white")

while True:
    clock.tick(60)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

    screen.blit(bg,(0,0))
    player.update()

    pygame.display.update()
