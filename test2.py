import pygame, sys, random
from pygame.locals import *

# check if one point is inside a rect object
def is_point_inside_rect(x, y, rect, bouncer_size):#ss =
    if (x > rect.left) and (x < rect.right-bouncer_size) and (y > rect.top) and (y < rect.bottom-bouncer_size):
        return True
    else:
        False

# get square pixel coordinates
def get_coordinates(SIZE):

    count = 1
    figures =[]
    for letter in range(len(letters)):
        lx = letterx + square_width*(count-1)
        figures.append(pygame.Rect(lx, lettery, square_width, square_height))
        count += 1


    xcor = []
    ycor = []
    for figure in figures:
        x = figure.left
        y = figure.top
        while x < figure.right:
            xcor.append(x)
            x += SIZE
    while y < figure.bottom:
        ycor.append(y)
        y += SIZE
    return xcor, ycor



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


# ----------------------------

# set up text
letters = 'H'

# set square's letter SIZE
square_width = int(window_width/9)
square_height = int(window_height/5)
print(square_width, square_height)

# get the x and y center of the window
centerx = window_surface.get_rect().centerx
centery = window_surface.get_rect().centery

# get x and y coordinates for the fisrt square's letter
letterx = centerx - (square_width/2)*len(letters)
lettery = centery - square_height/2


#------------------------------

# create bouncers
bouncers = []
SIZE = 4
for i in range(1080):
    color = random.choice(COLORS)
    direction = random.choice(DIRECTIONS)
    x = random.choice([x*SIZE for x in range(int(window_width/SIZE))])
    y = random.choice([y*SIZE for y in range(int(window_height/SIZE))])
    bouncers.append({'rect':pygame.Rect(x, y, SIZE, SIZE), 'SIZE':SIZE, 'dir':direction, 'color':color, 'speed':SIZE, 'speed1':SIZE})


# list of letter pixels
letter_pixel = []
final_pixels = []

# list of pixel coordinates
xcor, ycor = get_coordinates(SIZE)


# run the game loop
while True:
    # check for the QUIT event
    for event in pygame.event.get():
        if event.type == QUIT:
            points = 0
            for yr in ycor:
                for xr in xcor:
                    if (xr,yr) in letter_pixel:
                        points += 1
            print(len(letter_pixel), points)
            pygame.quit()
            sys.exit()

    # draw the white background onto the surface
    window_surface.fill(BLACK)


    #----------------------------------
    # draw  one square per letter and create Square structures
    count = 1
    squares =[]
    for letter in range(len(letters)):
        lx = letterx + square_width*(count-1)
        squares.append(pygame.Rect(lx, lettery, square_width, square_height))
        pygame.draw.rect(window_surface, BLACK, squares[letter])
        count += 1

    pygame.draw.rect(window_surface, BLACK, (centerx, centery, 1, 100))

    # draw the bouncers inside the letter
    for pixel in final_pixels:
        # draw the pixel onto the letter
        pygame.draw.rect(window_surface, pixel['color'], pixel['rect'])
    #--------------------------------

    # move and then draw bouncers
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
           # Multiply by SIZE to get the coordinates quicker
           # Check 'create bouncers' comment
           bouncer['speed'] = random.randint(1,2)*SIZE
           bouncer['speed'] = random.randint(1,2)*SIZE


        # check if the bouncer is inside a letter
        for square in squares:
            if (bouncer['rect'][0] in xcor) and (bouncer['rect'][1] in ycor):
                if ((bouncer['rect'][0], bouncer['rect'][1])) not in letter_pixel: #is_point_inside_rect(bouncer['rect'][0], bouncer['rect'][1], square, bouncer['SIZE'])
                    letter_pixel.append((bouncer['rect'][0], bouncer['rect'][1]))
                    final_pixels.append(bouncer)
                    bouncers.remove(bouncer)


        # draw the bouncer onto the surface
        pygame.draw.rect(window_surface, bouncer['color'], bouncer['rect'])


    # draw the window onto the screen
    pygame.display.update()
