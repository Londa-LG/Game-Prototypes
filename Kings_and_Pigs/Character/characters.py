import pygame

# Kings

class HumanKing(pygame.sprite.Sprite):
    
    def __init__(self,screen,pos):
        super().__init__()
        self.speed = 10
        self.screen = screen
        self.states = ["idle","run","jump","fall","land","attack","enter","exit","hit","dead"]
        self.animations = { "idle": [], "run": [], "jump": [], "fall": [],"land": [],"attack": [], "enter": [], "exit": [], "hit":[],"dead":[]}
        self.state = self.states[0]
        self.create_animations()
        self.animation_index = 0
        self.current_animation = self.animations[self.state]
        self.img = self.current_animation[self.animation_index]
        self.rect = self.img.get_rect()
        self.rect.midbottom = pos

    def move_right(self):
        self.rect.centerx += 5

    def move_left(self):
        self.rect.centerx -= 5

    def move_up(self):
        self.rect.centery -= 5

    def move_down(self):
        self.rect.centery += 5

    def perform_jump(self):
        pass

    def perform_attack(self):
        pass

    def perform_block(self):
        pass

    def take_damage(self):
        pass

    def animate(self):
        self.animation_index += 0.2
        if int(self.animation_index) < len(self.current_animation):
            self.img = self.current_animation[int(self.animation_index)]
        else:
            self.animation_index = 0
            self.img = self.current_animation[self.animation_index]

    def change_state(self,state):
        self.state = self.states[state]
        self.current_animation = self.animations[self.state]
        self.animation_index = 0
        self.display()

    def update(self):
        self.animate()
        self.display()

    def display(self):
        scaled_img = pygame.transform.scale2x(self.img)
        self.screen.blit(scaled_img, self.rect)
        
    def create_animations(self):
        # Create animation frames
        for animation in self.states:
            if animation == "idle":
                for i in range(0,11):
                    surface = pygame.image.load(f"Assets/King_Human/Idle/{i}.png").convert_alpha()
                    self.animations["idle"].append(surface)
            elif animation == "attack":
                for i in range(0,3):
                    surface = pygame.image.load(f"Assets/King_Human/Attack/{i}.png").convert_alpha()
                    self.animations["attack"].append(surface)
            elif animation == "dead":
                for i in range(0,4):
                    surface = pygame.image.load(f"Assets/King_Human/Dead/{i}.png").convert_alpha()
                    self.animations["dead"].append(surface)
            elif animation == "enter":
                for i in range(0,8):
                    surface = pygame.image.load(f"Assets/King_Human/Enter/{i}.png").convert_alpha()
                    self.animations["enter"].append(surface)
            elif animation == "exit":
                for i in range(0,8):
                    surface = pygame.image.load(f"Assets/King_Human/Exit/{i}.png").convert_alpha()
                    self.animations["exit"].append(surface)
            elif animation == "hit":
                for i in range(0,2):
                    surface = pygame.image.load(f"Assets/King_Human/Hit/{i}.png").convert_alpha()
                    self.animations["hit"].append(surface)
            elif animation == "jump":
                surface = pygame.image.load("Assets/King_Human/Jump/0.png").convert_alpha()
                self.animations["jump"] = surface
            elif animation == "fall":
                surface = pygame.image.load("Assets/King_Human/Jump/1.png").convert_alpha()
                self.animations["fall"] = surface
            elif animation == "land":
                surface = pygame.image.load("Assets/King_Human/Jump/2.png").convert_alpha()
                self.animations["land"] = surface
            elif animation == "run":
                for i in range(0,8):
                    surface = pygame.image.load(f"Assets/King_Human/Run/{i}.png").convert_alpha()
                    self.animations["run"].append(surface)


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
