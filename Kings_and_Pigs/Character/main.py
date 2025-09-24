import pygame 
from sys import exit
from characters import HumanKing
from settings import HEIGHT, WIDTH

pygame.init()
screen = pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption("Character prototypes")
clock = pygame.time.Clock()

player = HumanKing(screen,(100, 200))
bg = pygame.Surface((WIDTH,HEIGHT))
bg.fill("white")

while True:
    clock.tick(60)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_a or event.key == pygame.K_LEFT:
                player.change_state(3)
            if event.key == pygame.K_d or event.key == pygame.K_RIGHT:
                player.change_state(2)
            if event.key == pygame.K_w or event.key == pygame.K_SPACE or event.key == pygame.K_UP:
                player.perform_jump()

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_a or event.key == pygame.K_LEFT:
                player.change_state(1)
            if event.key == pygame.K_d or event.key == pygame.K_RIGHT:
                player.change_state(0)

    key_press = pygame.key.get_pressed()
    if key_press[pygame.K_a] or key_press[pygame.K_LEFT]:
        player.move_left()
    if key_press[pygame.K_d] or key_press[pygame.K_RIGHT]:
        player.move_right()


    screen.blit(bg,(0,0))
    player.update()

    pygame.display.update()
