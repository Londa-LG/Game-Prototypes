import pygame

# Kings

class HumanKing(pygame.sprite.Sprite):
    def __init__(self,screen,pos):
        super().__init__()
        self.screen = screen
        self.states = ["idle","run","jump","fall","land","attack","enter","exit","hit","dead"]
        self.create_animations()
        self.state = self.states[0]
        self.sprite_index = 0
        self.img = self.idle[self.sprite_index]
        self.rect = self.img.get_rect()
        self.rect.midbottom = pos

    def change_state(self,index):
        self.state = self.states[(index)]

    def animate(self):
        if self.state == "idle":
            # idle animation
            self.sprite_index += 0.2
            if int(self.sprite_index) < len(self.idle):
                self.img = self.idle[int(self.sprite_index)]
            else:
                self.sprite_index = 0
                self.img = self.idle[self.sprite_index]
        elif self.state == "run":
            # run animation
            self.sprite_index += 0.2
            if int(self.sprite_index) < len(self.run):
                self.img = self.run[int(self.sprite_index)]
            else:
                self.sprite_index = 0
                self.img = self.run[self.sprite_index]
        elif self.state == "jump":
            # jump animation
            if int(self.sprite_index) >= 1:
                self.sprite_index = 0
                self.change_state(3)
            else:
                self.sprite_index += 0.2
                self.img = self.jump
        elif self.state == "fall":
            # fall animation
            if int(self.sprite_index) >= 1:
                self.sprite_index = 0
                self.change_state(4)
            else:
                self.sprite_index += 0.2
                self.img = self.fall
        elif self.state == "land":
            # land animation
            if int(self.sprite_index) >= 1:
                self.sprite_index = 0
                self.change_state(0)
            else:
                self.sprite_index += 0.2
                self.img = self.land
        elif self.state == "attack":
            # attack animation
            self.sprite_index += 0.2
            if int(self.sprite_index) < len(self.attack):
                self.img = self.attack[int(self.sprite_index)]
            else:
                self.sprite_index = 0
                self.img = self.attack[(self.sprite_index)]
        elif self.state == "enter":
            # enter animation
            self.sprite_index += 0.2
            if int(self.sprite_index) < len(self.enter):
                self.img = self.enter[int(self.sprite_index)]
            else:
                self.sprite_index = 0
                self.img = self.enter[(self.sprite_index)]
        elif self.state == "exit":
            # exit animation
            self.sprite_index += 0.2
            if int(self.sprite_index) < len(self.exit):
                self.img = self.exit[int(self.sprite_index)]
            else:
                self.sprite_index = 0
                self.img = self.exit[(self.sprite_index)]
        elif self.state == "hit":
            # hit animation
            self.sprite_index += 0.2
            if int(self.sprite_index) < len(self.hit):
                self.img = self.hit[int(self.sprite_index)]
            else:
                self.sprite_index = 0
                self.img = self.hit[(self.sprite_index)]
        elif self.state == "dead":
            # dead animation
            self.sprite_index += 0.2
            if int(self.sprite_index) < len(self.dead):
                self.img = self.dead[int(self.sprite_index)]
            else:
                self.sprite_index = 0
                self.img = self.dead[(self.sprite_index)]

    def create_animations(self):
        self.attack = []
        self.idle = []
        self.run = []
        self.hit = []
        self.enter = []
        self.exit = []
        self.dead = []
        # Create animation frames
        for animation in self.states:
            if animation == "idle":
                for i in range(0,11):
                    surface = pygame.image.load(f"Assets/King_Human/Idle/{i}.png").convert_alpha()
                    self.idle.append(surface)
            elif animation == "attack":
                for i in range(0,3):
                    surface = pygame.image.load(f"Assets/King_Human/Attack/{i}.png").convert_alpha()
                    self.attack.append(surface)
            elif animation == "dead":
                for i in range(0,4):
                    surface = pygame.image.load(f"Assets/King_Human/Dead/{i}.png").convert_alpha()
                    self.dead.append(surface)
            elif animation == "enter":
                for i in range(0,8):
                    surface = pygame.image.load(f"Assets/King_Human/Enter/{i}.png").convert_alpha()
                    self.enter.append(surface)
            elif animation == "exit":
                for i in range(0,8):
                    surface = pygame.image.load(f"Assets/King_Human/Exit/{i}.png").convert_alpha()
                    self.exit.append(surface)
            elif animation == "hit":
                for i in range(0,2):
                    surface = pygame.image.load(f"Assets/King_Human/Hit/{i}.png").convert_alpha()
                    self.hit.append(surface)
            elif animation == "jump":
                surface = pygame.image.load("Assets/King_Human/Jump/0.png").convert_alpha()
                self.jump = surface
            elif animation == "fall":
                surface = pygame.image.load("Assets/King_Human/Jump/1.png").convert_alpha()
                self.fall = surface
            elif animation == "land":
                surface = pygame.image.load("Assets/King_Human/Jump/2.png").convert_alpha()
                self.land = surface
            elif animation == "run":
                for i in range(0,8):
                    surface = pygame.image.load(f"Assets/King_Human/Run/{i}.png").convert_alpha()
                    self.run.append(surface)

    def update(self):
        self.animate()
        self.display()

    def display(self):
        scaled_img = pygame.transform.scale2x(self.img)
        self.screen.blit(scaled_img, self.rect)


class PigKing(pygame.sprite.Sprite):
    pass

# Pigs

class Pig(pygame.sprite.Sprite):
    pass

class ThrowingBox(Pig):
    pass

class ThrowingBomb(Pig):
    pass

class HidenInBox(Pig):
    pass

class WithMatch(Pig):
    pass
