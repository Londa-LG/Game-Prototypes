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

    keys = pygame.key.get_pressed()
    if keys[pygame.K_a] or keys[pygame.K_LEFT]:
        player.move_left()
    if keys[pygame.K_d] or keys[pygame.K_RIGHT]:
        player.move_right()
    if keys[pygame.K_w] or keys[pygame.K_UP]:
        player.perform_jump()

    screen.blit(bg,(0,0))
    player.update()

    pygame.display.update()
