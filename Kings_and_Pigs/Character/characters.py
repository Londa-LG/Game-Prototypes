import pygame

# Kings

class HumanKing(pygame.sprite.Sprite):
    def __init__(self,dt):
        super().__init__()
        self.states = [
            "idle",
            "run",
            "jump",
            "attack",
            "enter",
            "exit",
            "hit",
            "dead"
        ]
        self.create_animations()
        self.state = self.state[0]

        def animate(self):
            if self.state == "idle":
                # idle animation
                pass
            elif self.state == "run":
                # run animation
                pass
            elif self.state == "jump":
                # jump animation
                pass
            elif self.state == "attack":
                # attack animation
                pass
            elif self.state == "enter":
                # enter animation
                pass
            elif self.state == "exit":
                # exit animation
                pass
            elif self.state == "hit":
                # hit animation
                pass
            elif self.state == "dead":
                # run run animation
                pass


        def create_animations(self):
            location = "01-King Human"
            self.attack = []
            self.idle = []
            self.jump = []
            self.run = []
            self.hit = []
            self.enter = []
            self.exit = []
            self.dead = []
            # Create animation frames
            for animation in self.states:
                if animation == "idle":
                    for i in range(0,12):
                        try:
                            self.idle.append(pygame.image.load(str(location + f"/Idle/{i}.png")))
                        except:
                            pass
                elif animation == "attack":
                    for i in range(0,12):
                        try:
                            self.idle.append(pygame.image.load(str(location + f"/Attack/{i}.png")))
                        except:
                            pass
                elif animation == "dead":
                    for i in range(0,12):
                        try:
                            self.idle.append(pygame.image.load(str(location + f"/Dead/{i}.png")))
                        except:
                            pass
                elif animation == "enter":
                    for i in range(0,12):
                        try:
                            self.idle.append(pygame.image.load(str(location + f"/Enter/{i}.png")))
                        except:
                            pass
                elif animation == "exit":
                    for i in range(0,12):
                        try:
                            self.idle.append(pygame.image.load(str(location + f"/Exit/{i}.png")))
                        except:
                            pass
                elif animation == "hit":
                    for i in range(0,12):
                        try:
                            self.idle.append(pygame.image.load(str(location + f"/Hit/{i}.png")))
                        except:
                            pass
                elif animation == "jump":
                    for i in range(0,12):
                        try:
                            self.idle.append(pygame.image.load(str(location + f"/Jump/{i}.png")))
                        except:
                            pass
                elif animation == "run":
                    for i in range(0,12):
                        try:
                            self.idle.append(pygame.image.load(str(location + f"/Run/{i}.png")))
                        except:
                            pass


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
