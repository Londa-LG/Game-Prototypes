import pygame
import time
from levels import Menu,GamePlay
from sys import exit

class Game:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((800,480))
        pygame.display.set_caption("Level switch")
        self.clock = pygame.time.Clock()
        self.menu_view = Menu(self.screen)
        self.game_view = GamePlay(self.screen)
        self.running = True
        self.state = "menu"

    def wait(self):
        for remaining in range(10, 0, -1):
            print("Remaining: ",remaining)
            time.sleep(1)
        self.switch_level()

    def game(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()

        self.game_view.update()
        pygame.display.update()
        self.clock.tick(60)
        self.wait()

    def menu(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()

        self.menu_view.update()
        pygame.display.update()
        self.clock.tick(60)
        self.wait()

    def switch_level(self):
        if self.state == "menu":
            self.state = "game"
        else:
            self.state = "menu"

    def state_manager(self):
        if self.state == "menu":
            self.menu()
        if self.state == "game":
            self.game()
        

def main():
    game = Game()
    clock = pygame.time.Clock()

    while True:
        game.state_manager()
        clock.tick(60)

if __name__ == "__main__":
    main()
