#init
print("program start. . .")
import random, math
print("importing PyGame. . .")
import pygame
from pygame.locals import *
print("importing sub.py. . .")
from sub import Sub
print("importing freighter.py. . .")
from freighter import Freighter
print("importing functions.py. . .")
from functions import *

#simulation constants
print("setting simulation constants. . .")
framerate = 40
SCREENRECT = Rect(0, 0, 1012, 759)

# Initialize pygame
print("initializing PyGame. . .")
pygame.init()
if pygame.mixer and not pygame.mixer.get_init():
    print ('Warning, no sound')
    pygame.mixer = None

# Set the display mode
print("setting display mode. . .")
winstyle = 1  # |FULLSCREEN
bestdepth = pygame.display.mode_ok(SCREENRECT.size, winstyle, 32)
screen = pygame.display.set_mode(SCREENRECT.size, winstyle, bestdepth)

#Load images, assign to sprite classes
#(do this before the classes are used, after screen setup)
print("loading images. . .")
Freighter.images = [load_image('greenDot.png')]
Sub.images = [load_image('submarine.png')]

#decorate the game window
print("decorating game window. . .")
icon = pygame.transform.scale(Sub.images[0], (32, 32))
pygame.display.set_icon(icon)
pygame.display.set_caption('Atlantic Hunt')
pygame.mouse.set_visible(0)

#create the background, tile the bgd image
print("creating the background. . .")
bgdtile = load_image('background.png')
background = pygame.Surface(SCREENRECT.size)
for x in range(0, SCREENRECT.width, bgdtile.get_width()):
    background.blit(bgdtile, (x, 0))
screen.blit(background, (0,0))
pygame.display.flip()

#initialize game groups
print("initializing game groups. . .")
subs = pygame.sprite.Group()
freighters = pygame.sprite.Group()
all = pygame.sprite.RenderUpdates()

#make default groups for each sprite class
print("making default groups. . .")
Freighter.containers = freighters, all
Sub.containers = subs, all

#create starting sprites
print("creating starting sprites. . .")
sally = Sub(SCREENRECT, 'sally')
sally.add(subs)
sally.add(all)
fred = Freighter(SCREENRECT, 'fred')
fred.add(freighters)
fred.add(all)

#setup the clock
print("setting up the clock. . .")
clock = pygame.time.Clock()

#running the simulation
frame = 0
print("running the simulation. . .")

while fred.alive():

    #clear the sprites
    all.clear(screen, background)
            
   #check for detection 
    interceptions=pygame.sprite.groupcollide(subs, freighters, 0, 0)
    for sub in interceptions.keys():
        target = interceptions[sub][0]
        if sub.detect(target):
            print("kill!")
            target.kill() 

    #update sprites
    for thing in all:
        thing.updateData(subs, freighters)
        thing.update()

 
    #draw the scene
    scene = all.draw(screen)
    pygame.display.update(scene)

    #cap framerate
    clock.tick(framerate)

    #print frame number
    #print("frame " + str(frame) + ", Fred status: " + str(fred.alive()))
    frame += 1

#end the simulation
pygame.time.wait(1000)
pygame.quit()



















