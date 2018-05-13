import pygame
class Sub(pygame.sprite.Sprite):
    
    def __init__(self, SCREENRECT):
        self.speed = 8
        pygame.sprite.Sprite.__init__(self)
        self.image = self.images[0]
        self.rect = self.image.get_rect(midbottom=SCREENRECT.midbottom)
        self.reloading = 0
        self.origtop = self.rect.top
        self.facing = -1
        self.SCREENRECT=SCREENRECT
        self.direction = 1.57

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

    def detect(self,dist,time,size):
        print("checking for detection. . .")

        #detection algorithim
        import random
        detected=random.random()>0.5

        if detected == True:
            print("target detected!")
        else:
            print("target not detected!")
            
        return detected

    def surface(self):
        self.speed = 20

    def submerge(self):
        self.speed = 8

        
