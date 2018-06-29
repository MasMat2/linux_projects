import pygame, sys, random
from pygame.locals import *

# set up pygame
pygame.init()
main_clock = pygame.time.Clock()

# set up the window
window_width = 200
window_height = 200
window_surface = pygame.display.set_mode((window_width, window_height), 0, 32)
pygame.display.set_caption('Crazy names men')

# set up direction variables
DOWNLEFT = 1
DOWNRIGHT = 3
UPLEFT = 7
UPRIGHT= 9
DIRECTIONS =[DOWNLEFT, DOWNRIGHT, UPLEFT, UPRIGHT]

# set up the colors
BLACK = (40, 44, 52)
WHITE =(255, 255, 255)
GREEN = (150, 253, 109)
RED = (254, 55, 190)
BLUE = (87, 199, 208)
PURPLE = (203, 103, 211)
RED1 =(242, 15, 61)
BROWN = (215,168, 142)
ORANGE = (255, 176, 97)
YELLOW = (238, 226, 0)
COLORS = [GREEN, RED, BLUE, PURPLE, RED1, BROWN, ORANGE, YELLOW]

movespeed = 2
movespeed1 = 2

#create bouncer
bouncers = []
for i in range(3):
    color = random.choice(COLORS)
    direction = random.choice(DIRECTIONS)
    x = random.randint(0,window_width)
    y = random.randint(0,window_height)
    bouncers.append({'rect':pygame.Rect(x, y, random.choice([2]), random.choice([2])), 'dir':direction, 'color':color, 'speed':10, 'speed1':10})

# run the game loop
while True:

    # check for the QUIT event
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

    # draw the background onto the surface
    window_surface.fill(BLACK)

    # draw bouncers
    for bouncer in bouncers:
        # move the bouncer data structure
        if bouncer['dir'] == DOWNLEFT:
            bouncer['rect'].left -= bouncer['speed']
            bouncer['rect'].top += bouncer['speed1']
        if bouncer['dir'] == DOWNRIGHT:
            bouncer['rect'].left += bouncer['speed']
            bouncer['rect'].top += bouncer['speed1']
        if bouncer['dir'] == UPLEFT:
            bouncer['rect'].left -= bouncer['speed']
            bouncer['rect'].top -= bouncer['speed1']
        if bouncer['dir'] == UPRIGHT:
            bouncer['rect'].left += bouncer['speed']
            bouncer['rect'].top -= bouncer['speed1']


        # check if the bouncer has move out the window
        if bouncer['rect'].top < 0:
            if bouncer['dir'] == UPLEFT:
                bouncer['dir'] = DOWNLEFT
            if bouncer['dir'] == UPRIGHT:
                bouncer['dir'] = DOWNRIGHT
        if bouncer['rect'].right > window_width: # bug the dir chenged from 3 to 1 for a mistake in the > sign
            if bouncer['dir'] == UPRIGHT:
                bouncer['dir'] = UPLEFT
            if bouncer['dir'] == DOWNRIGHT:
                bouncer['dir'] = DOWNLEFT
        if bouncer['rect'].bottom > window_height:
            if bouncer['dir'] == DOWNLEFT:
                bouncer['dir'] = UPLEFT
            if bouncer['dir'] == DOWNRIGHT:
                bouncer['dir'] = UPRIGHT
        if bouncer['rect'].left < 0:
            if bouncer['dir'] == UPLEFT:
                bouncer['dir'] = UPRIGHT
            if bouncer['dir'] == DOWNLEFT:
                bouncer['dir'] = DOWNRIGHT
        if (bouncer['rect'].top < 0 or bouncer['rect'].right > window_width or
           bouncer['rect'].bottom > window_height or bouncer['rect'].left < 0):
           bouncer['speed'] = 5#random.randint(9,10)
           bouncer['speed1'] = 6#random.randint(9,10)

        # draw the bouncer onto the surface

        pygame.draw.rect(window_surface, bouncer['color'], bouncer['rect'])


    # display update
    pygame.display.update()
    main_clock.tick(20)
