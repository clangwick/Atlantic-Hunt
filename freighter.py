import pygame
class Freighter(pygame.sprite.Sprite):
    
    def __init__(self, SCREENRECT):
        self.speed = 10
        pygame.sprite.Sprite.__init__(self)
        self.image = self.images[0]
        self.rect = self.image.get_rect(midleft=SCREENRECT.midleft)
        self.reloading = 0
        self.origtop = self.rect.top
        self.facing = -1
        self.SCREENRECT=SCREENRECT
        self.direction = 0

    def move(self,direction):
        import math
        self.rect.move_ip(self.speed*math.cos(direction), self.speed*math.sin(direction))
        if not self.SCREENRECT.contains(self.rect):
            self.direction += 3.14
            self.move(self.direction)
        self.rect = self.rect.clamp(self.SCREENRECT)

    def update(self):
        import random
        self.direction += (random.random()-0.5)*0.52
        self.move(self.direction)

    def detect(self,dist,time,size,submerged):
        import random
        detected=random.random()>0.5
        return detected
