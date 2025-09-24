import pygame
from settings import HEIGHT, WIDTH

# Kings

class HumanKing(pygame.sprite.Sprite):
    
    def __init__(self,screen,pos):
        super().__init__()
        self.speed = 10
        self.screen = screen
        self.states = ["idleL","idleR","runL","runR","jump","fall","land","attack","enter","exit","hit","dead"]
        self.animations = { "idleL": [], "idleR": [], "runL": [], "runR": [], "jump": [], "fall": [],"land": [],"attack": [], "enter": [], "exit": [], "hit":[],"dead":[]}
        self.state = self.states[0]
        self.create_animations()
        self.animation_index = 0
        self.current_animation = self.animations[self.state]
        self.img = self.current_animation[self.animation_index]
        self.rect = self.img.get_rect()
        self.rect.midbottom = pos
        self.vel = 0

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

    def boundary(self):
        if self.rect.bottom >= HEIGHT:
            self.rect.bottom = HEIGHT;
            self.vel = 0
        if self.rect.right > WIDTH:
            self.rect.right = WIDTH;
        if self.rect.left <= 0:
            self.rect.left = 0;

    def gravity(self):
        self.vel = self.vel + 0.2
        self.rect.centery += self.vel

    def animate(self):
        self.animation_index += 0.2
        if self.state == "jump" or self.state == "fall":
            pass
        else:
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
        self.boundary()
        self.gravity()
        self.display()

    def display(self):
        #scaled_img = pygame.transform.scale2x(self.img)
        self.screen.blit(self.img, self.rect)
        
    def create_animations(self):
        # Create animation frames
        for animation in self.states:
            if animation == "idleR":
                for i in range(0,11):
                    self.animations["idleR"].append(pygame.transform.flip(self.animations["idleL"][i], flip_x = True, flip_y = False))
            if animation == "idleL":
                for i in range(0,11):
                    surface = pygame.image.load(f"Assets/King_Human/Idle/{i}.png").convert_alpha()
                    self.animations["idleL"].append(surface)
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
            elif animation == "runL":
                for i in range(0,8):
                    surface = pygame.image.load(f"Assets/King_Human/Run/{i}.png").convert_alpha()
                    self.animations["runL"].append(surface)
            elif animation == "runR":
                for i in range(0,8):
                    self.animations["runR"].append(pygame.transform.flip(self.animations["runL"][i], flip_x = True, flip_y = False))




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
