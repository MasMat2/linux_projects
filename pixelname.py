import pygame, sys, random, time #tiem sleep tests
from pygame.locals import *


def get_coordinates(SIZE):

    figure = (pygame.Rect(letterx, lettery, square_width, square_height))

    xcor = []
    ycor = []

    x = figure.left
    y = figure.top
    while x < figure.right:
        xcor.append(x)
        x += SIZE
        while y < figure.bottom:
            ycor.append(y)
            y += SIZE
    return xcor, ycor

def move_pixel(bouncer,loop):
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

            if loop == loops-1: ## Some  pixels would have to change direction twice and not return to the origin
                return 0    ## Delete this lines and pixels with speeds 8 or higher number won't get to the origin

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


# set up pygame
pygame.init()

# set up the window
window_width = 1080
window_height = 720
window_surface = pygame.display.set_mode((window_width, window_height), 0, 32)
pygame.display.set_caption('TEST 2')

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


# set square's letter SIZE
square_width = int(window_width/9)
square_height = int(window_height/5)

# get the x and y center of the window
centerx = window_surface.get_rect().centerx
centery = window_surface.get_rect().centery

# get x and y coordinates for the fisrt square's letter
letterx = centerx - (square_width/2)
lettery = centery - square_height/2

# list of pixel coordinates
SIZE = 4
xcor, ycor = get_coordinates(SIZE)

# create bouncers
bouncers = []
SIZE = 4
for x in xcor:
    for y in ycor:
        color = random.choice(COLORS)
        direction = random.choice(DIRECTIONS)
        ran_speed = random.randint(1,10) # x cannot be 8
        if ran_speed < 5:
            ran_speed1 = random.randint(5,10) # y cannot be 9 why? Maybe mathematics
        else:
            ran_speed1 = random.randint(1,5)
        bouncers.append({'rect':pygame.Rect(x, y, SIZE, SIZE), 'SIZE':SIZE, 'dir':direction, 'color':color, 'speed':ran_speed, 'speed1':ran_speed1, 'origin':(x,y), 'loop': 0, 'or_dir':direction})

# list of letter pixels
letter_pixel = [] #!
final_pixels = []
bre = 0

for bouncer in bouncers:
    loops = random.randint(200,300)
    for loop in range(loops):
        move_pixel(bouncer, loop)
    bouncer['loops'] = loops


for bouncer in bouncers: #!
    new_dir = {1:9, 9:1, 3:7, 7:3, 2:8, 8:2, 4:6, 6:4}
    bouncer['dir'] = new_dir[bouncer['dir']]

# run the game loop
while True:
    # check for the QUIT event
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()


    # draw the white background onto the surface
    window_surface.fill(BLACK)
    # draw the bouncers inside the letter
    for pixel in final_pixels:
        # draw the pixel onto the letter
        pygame.draw.rect(window_surface, pixel['color'], pixel['rect'])
    #--------------------------------

    # move and then draw bouncers
    copybouncers = bouncers[:]
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


        bouncer['loop'] += 1


        if (bouncer['rect'][0], bouncer['rect'][1]) == bouncer['origin'] and bouncer['loop'] >= bouncer['loops']:
            final_pixels.append(bouncer)
            copybouncers.remove(bouncer)

        # draw the bouncer onto the surface
        pygame.draw.rect(window_surface, bouncer['color'], bouncer['rect'])


    bouncers = copybouncers
    # draw the window onto the screen
    pygame.display.update()
