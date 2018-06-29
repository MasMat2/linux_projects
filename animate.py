import pygame, sys, time, random
from pygame.locals import *

# set up pygame
pygame.init()

# set up the window
WINDOWWIDTH = int(1280/2)
WINDOWHEIGHT = 748
windowSurface = pygame.display.set_mode((WINDOWWIDTH, WINDOWHEIGHT), 0, 32)
pygame.display.set_caption('ANIMAAATION moda fucker')

# set up direction variables
DOWNLEFT = 1
DOWNRIGHT = 3
UPLEFT = 7
UPRIGHT = 9

ms = 4
ms2 = 6

# set up the colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (254, 55, 190)
RW = (254, 105, 206)
GREEN =(150, 253, 109)
BLUE = (87, 199, 208)
PURPLE = (203, 103, 211)

# set up the data structure
b1 = {'rect':pygame.Rect(300, 80, 50, 100), 'color':RED, 'dir':UPRIGHT}
b2 = {'rect':pygame.Rect(200, 200, 20, 20), 'color':GREEN, 'dir':UPLEFT}
b3 = {'rect':pygame.Rect(100, 150, 60, 60), 'color':BLUE, 'dir':DOWNLEFT}
b4 = {'rect':pygame.Rect(200, 100, 40, 30), 'color':PURPLE, 'dir':UPLEFT}
blocks = [b1, b2, b3, b4]

def cms(ms):
    ms = random.randint(6,8)
    ms2 = random.randint(6,8)
    return ms, ms2

count = 0
cond = True
# run the game loop
while True:
    if cond:
        cond = blocks[3]['rect'][2] <= 200
        blocks[3]['rect'][2] += 2
        blocks[3]['rect'][3] += 2
    else:
        cond = blocks[3]['rect'][2] <= 3
        blocks[3]['rect'][2] -= 2
        blocks[3]['rect'][3] -= 2

    count += 1
    if count % 100 == 0:
        if random.randint(0,10) % 2 == 0:
            a = [RED, BLUE, GREEN]
            random.shuffle(a)
            b1['color'], b2['color'], b3['color'] = a[0], a[1], a[2]

    # check for the QUIT event
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

    # draw the black background onto the surface
    windowSurface.fill(BLACK)

    pygame.draw.rect(windowSurface, RED, (630, 0, 10, 10))
    pygame.draw.rect(windowSurface, BLUE, (630, 50, 10, 10))
    pygame.draw.rect(windowSurface, GREEN, (630, 100, 10, 10))
    pygame.draw.rect(windowSurface, PURPLE, (630, 150, 10, 10))

    for b in reversed(blocks):
        # move the block data structure
        if b['dir'] == DOWNLEFT:
            b['rect'].left -= ms
            b['rect'].top += ms2
        if b['dir'] == DOWNRIGHT:
            b['rect'].left += ms
            b['rect'].top += ms2
        if b['dir'] == UPLEFT:
            b['rect'].left -= ms2
            b['rect'].top -= ms
        if b['dir'] == UPRIGHT:
            b['rect'].left += ms2
            b['rect'].top -= ms

        # check if the block has moved out of the window
        if b['rect'].top < 0:
            ms, ms2 = cms(ms)
            # block has moved past the top
            if b['dir'] == UPLEFT:
                b['dir'] = DOWNLEFT
            if b['dir'] == UPRIGHT:
                b['dir'] = DOWNRIGHT
        if b['rect'].bottom > WINDOWHEIGHT:
            ms, ms2 = cms(ms)
            # block has moved past the bottom
            if b['dir'] == DOWNLEFT:
                b['dir'] = UPLEFT
            if b['dir'] == DOWNRIGHT:
                b['dir'] = UPRIGHT
        if b['rect'].left < 0:
            ms, ms2 = cms(ms)
            # block has moved past the left side
            if b['dir'] == DOWNLEFT:
                b['dir'] = DOWNRIGHT
            if b['dir'] == UPLEFT:
                b['dir'] = UPRIGHT
        if b['rect'].right > WINDOWWIDTH:
            ms, ms2 = cms(ms)
            # block has moved past the right side
            if b['dir'] == DOWNRIGHT:
                b['dir'] = DOWNLEFT
            if b['dir'] == UPRIGHT:
                b['dir'] = UPLEFT
        # draw the block onto the surface
        pygame.draw.rect(windowSurface, b['color'], b['rect'])

        # draw the window onto the screen
    pygame.display.update()
    time.sleep(0.02)
