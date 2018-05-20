import pygame
class Sub(pygame.sprite.Sprite):
    
    def __init__(self, SCREENRECT, name):
        self.speed = 8
        self.coordinates = [0,0,6371000]
        pygame.sprite.Sprite.__init__(self)
        self.image = self.images[0]
        self.rect = self.image.get_rect(midbottom=SCREENRECT.midbottom)
        self.fuel = 100
        self.origtop = self.rect.top
        self.SCREENRECT=SCREENRECT
        self.heading = 1.57
        self.detectRange = 15
        self.turnRate = 30
        self.state = 'hunting'
        self.target = 'none'
        self.name = name

    def move(self,heading):
        import math
        

        
        self.rect.move_ip(int(self.speed*math.cos(heading)), int(self.speed*math.sin(heading)))
        if not self.SCREENRECT.contains(self.rect):
            self.heading += 3.14
            self.move(self.heading)
        self.rect = self.rect.clamp(self.SCREENRECT)

    def updateData(self, subs, freighters):
        self.subs = subs
        self.freighters = freighters

    def update(self):
        if self.state == 'sunk':
            errorMessage = "error: submarine " + self.name + " has been sunk" 
            return errorMessage

        elif self.state == 'hunting':
            self.hunt()
                 
        elif self.state == 'chasing':
            self.chase()

    def startChase(self, fred):
        self.state = 'chasing'
        self.target = fred

    def chase(self):
        
        #attack target if in range
            
        #pursue target
        if abs(self.heading-self.target.dir) <= self.turnRate or True:
            self.heading = self.target.heading

    def hunt(self):
        #search for freighters
        

        #move randomly if no target found
        if self.state == "hunting":
            import random
            self.heading += (random.random()-0.5)*0.017453293*self.turnRate
            self.move(self.heading)


    def detect(self,fred):
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

    
        
