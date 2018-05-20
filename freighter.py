import pygame
class Freighter(pygame.sprite.Sprite):
    
    def __init__(self, SCREENRECT,name):
        self.speed = 10
        self.coordinates = [0,0,6371000]
        pygame.sprite.Sprite.__init__(self)
        self.image = self.images[0]
        self.rect = self.image.get_rect(midleft=SCREENRECT.midleft)
        self.origtop = self.rect.top
        self.SCREENRECT=SCREENRECT
        self.heading = 0
        self.name = name

    def move(self,heading):
        import math
        self.rect.move_ip(self.speed*math.cos(heading), self.speed*math.sin(heading))
        if not self.SCREENRECT.contains(self.rect):
            self.heading += 3.14
            self.move(self.heading)
        self.rect = self.rect.clamp(self.SCREENRECT)


    def updateData(self, subs, freighters):
        self.subs = subs
        self.freighters = freighters
        
    def update(self):
        import random
        self.heading += (random.random()-0.5)*0.52
        self.move(self.heading)

    def detect(self,dist,time,size,submerged):
        import random
        detected=random.random()>0.5
        return detected
