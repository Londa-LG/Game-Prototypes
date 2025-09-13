import pygame
import math
from characters import *
        

pygame.init()
screen = pygame.display.set_mode((800,600))
pygame.display.set_caption("Galactic wars")
clock = pygame.time.Clock()
running = True
dt = 0

# Creating player
p = pygame.Surface((60,60))
p.fill("orange")
rect = p.get_rect(center =(0,0))

# Settings
destination = pygame.Vector2(400,300)
speed = 5

# Calculating unit vector x and y components
height = destination[1] - rect.centery
width = destination[0] - rect.centerx
dist = math.sqrt((height ** 2) + (width ** 2)) 
uv_x = (destination[0] - rect.centerx) / dist
uv_y = (destination[1] - rect.centery) / dist


while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill("black")
    screen.blit(p,rect)

    # Move till reaching destination
    if rect.centerx != destination[0] or rect.centery != destination[1]:
        rect.centerx += (uv_x * speed)
        rect.centery += (uv_y * speed)

    pygame.display.flip()

    dt = clock.tick(60) / 1000

pygame.quit()


