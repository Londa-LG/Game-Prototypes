import pygame
from sys import exit
from obj import Player, Wall

pygame.init()
screen = pygame.display.set_mode((800,600))
pygame.display.set_caption("Collision")
clock = pygame.time.Clock()

player = Player(screen)
bg = pygame.Surface((800,600))
bg.fill("white")
wall = Wall(screen)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

    screen.blit(bg,(0,0))
    player.update()
    wall.update()

    if player.rect.colliderect(wall.rect):
        if player.rect.midleft <= wall.rect.midright:
            player.rect.left = wall.rect.right

    pygame.display.update()
    clock.tick(60)
