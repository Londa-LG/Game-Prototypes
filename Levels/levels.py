import pygame
from sys import exit

pygame.init()
screen = pygame.display.set_mode((800,480))
clock = pygame.time.Clock()

class Menu:
    def __init__(self,screen):
        self.screen = screen
        self.surface = pygame.Surface((800,480))
        self.surface.fill("blue")

    def update(self):
        self.screen.blit(self.surface,(0,0))

class GamePlay:
    def __init__(self,screen):
        self.screen = screen
        self.surface = pygame.Surface((800,480))
        self.surface.fill("orange")

    def update(self):
        self.screen.blit(self.surface,(0,0))

        

