import pygame

class Enemy_Projectile:
    def __init__(self):
        pass

class Player_Projectile:
    def __init__(self):
        pass

class Shooter:
    speed = 2
    
    def __init__(self,screen,target):
        self.target = target
        self.screen = screen
        self.surface = pygame.Surface((30,30))
        self.surface.fill("yellow")
        self.rect = self.surface.get_rect()

    def chase(self):
        pass

    def shoot(self):
        pass

    def display(self):
        self.screen.blit(self.surface, self.rect)

    def update(self):
        self.chase()
        self.shoot()
        self.display()

class Chaser:
    speed = 3

    def __init__(self,screen,target):
        self.target = target
        self.screen = screen
        self.surface = pygame.Surface((30,30))
        self.surface.fill("red")
        self.rect = self.surface.get_rect()

    def chase(self):
        if self.target.rect.centerx < self.rect.centerx:
            self.rect.centerx = self.rect.centerx - self.speed
            if self.target.rect.centery < self.rect.centery:
                self.rect.centery = self.rect.centery - self.speed
            elif self.target.rect.centery > self.rect.centery:
                self.rect.centery = self.rect.centery + self.speed
        elif self.target.rect.centerx > self.rect.centerx:
            self.rect.centerx = self.rect.centerx + self.speed
            if self.target.rect.centery < self.rect.centery:
                self.rect.centery = self.rect.centery - self.speed
            elif self.target.rect.centery > self.rect.centery:
                self.rect.centery = self.rect.centery + self.speed
        else:
            if self.target.rect.centery < self.rect.centery:
                self.rect.centery = self.rect.centery - self.speed
            elif self.target.rect.centery > self.rect.centery:
                self.rect.centery = self.rect.centery + self.speed
            
    def display(self):
        self.screen.blit(self.surface, self.rect)

    def update(self):
        self.chase()
        self.display()

class Player:
    speed = 10

    def __init__(self,screen):
        self.screen = screen
        self.surface = pygame.Surface((60,60))
        self.surface.fill("orange")
        self.rect = self.surface.get_rect(midbottom =(300,300))

    def shoot(self):
        pass

    def update(self):
        # Detect keyboard input
        keys = pygame.key.get_pressed()
        if keys[pygame.K_w]:
            self.move_up()
        if keys[pygame.K_s]:
            self.move_down()
        if keys[pygame.K_a]:
            self.move_left()
        if keys[pygame.K_d]:
            self.move_right()

        self.display()

    def display(self):
        self.screen.blit(self.surface,self.rect)

    def move_left(self):
        self.rect.centerx -= self.speed
        
    def move_right(self):
        self.rect.centerx += self.speed

    def move_up(self):
        self.rect.centery -= self.speed
        
    def move_down(self):
        self.rect.centery += self.speed
        
