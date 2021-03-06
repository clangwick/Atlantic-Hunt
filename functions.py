import os.path, pygame
def load_image(file):
    "loads an image, prepares it for play"
    file = os.path.join(os.path.split(os.path.abspath(__file__))[0], 'data', file)
    try:
        surface = pygame.image.load(file)
    except pygame.error:
        raise SystemExit('Could not load image "%s" %s'%(file, pygame.get_error()))
    return surface.convert()

def load_images(*files):
    imgs = []
    for file in files:
        imgs.append(load_image(file))
    return imgs

def load_sound(file):
    if not pygame.mixer: return dummysound()
    file = os.path.join(main_dir, 'data', file)
    try:
        sound = pygame.mixer.Sound(file)
        return sound
    except pygame.error:
        print ('Warning, unable to load, %s' % file)
    return dummysound()

def distance( loc1, loc2 ):
    dist = ((loc1[0]-loc2[0])**2 + (loc1[1]-loc2[1])**2)**0.5
    return dist
