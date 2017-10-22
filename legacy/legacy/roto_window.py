import sys, pygame;
from roto_file import getFileSuffix
#
#   preview window
#

from math import floor
from roto_settings import *;

def display(filename, src, num, fps, imageType):
    frameInterval = 1000 / fps;
    src += filename
    
    print("Initialising preview @", fps, "fps!");
    
    pygame.init();
    
    width = 800;
    
    if imageType == '-png':
        images = [pygame.image.load( src + getFileSuffix(n, ".png")) for n in range(num)];
    else:
        images = [pygame.image.load( src + getFileSuffix(n, ".tiff")) for n in range(num)];
    
    w, h = images[0].get_rect().size;
    scale, rh = width / w, h / w;
    
    if w < 800:
        width = 800
        scale, rh = 1, h / w
    
    images = [pygame.transform.scale(im, (width, floor(width * rh))) for im in images];
    screen = pygame.display.set_mode((width, floor(width * rh)), 0, 32);
    frame = 0;
    timeNow = pygame.time.get_ticks();
    paused = False;
    
    while True:
        for e in pygame.event.get():
            if e.type == pygame.QUIT:
                sys.exit();
            if e.type == pygame.KEYDOWN:
                if e.key == pygame.K_SPACE:
                    paused = paused ^ True;
                    if not paused:
                        timeNow = pygame.time.get_ticks();
        
        if not paused:
            if pygame.time.get_ticks() - timeNow > frameInterval:
                timeNow = pygame.time.get_ticks();
                frame = (frame + 1) % len(images);

            screen.fill((200, 200, 200));
            screen.blit(images[frame], (0, 0));
            pygame.display.flip();