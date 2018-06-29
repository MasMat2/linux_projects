import pygame, sys, random
from pygame.locals import *

def do_rects_overlap(rect1, rect2):
    for a, b in [(rect1, rect2), (rect2, rect1)]:
        # Check if a's corners are inside b
        if((is_point_inside_rect(a.left, a.top, b)) or
            (is_point_inside_rect(a.left, a.bottom, b)) or
            (is_point_inside_rect(a.right, a.top, b)) or
            (is_point_inside_rect(a.right, a.bottom, b))):
            return True

    return False

def is_point_inside_rect(x, y, rect):
    if (x > rect.left) and (x < rect.right) and (y > rect.top) and (y < rect.bottom):
        return True
    else:
        False


# set up pygame
pygame.init()
main_clock = pygame.time.Clock()

# set up the window
window_width = 1080
window_height = 720
window_surface = pygame.display.set_mode((window_width, window_height), 0, 32)
pygame.display.set_caption('Collision detection nigga!!')

# set up direction variables
DOWNLEFT = 1
DOWNRIGHT = 3
UPLEFT = 7
UPRIGHT = 9

movespeed = 10
movespeed1 = 10

# set up the colors
BLACK = (40, 44, 52)
WHITE =(255, 255, 255)
GREEN = (150, 253, 109)
RED = (254, 55, 190)
BLUE = (87, 199, 208)

# set up the bouncer and food data structures
food_counter = 0
NEW_FOOD = 0
FOOD_SIZE = 20
x = [FOOD_SIZE*sub for sub in range(int(window_width/FOOD_SIZE))]
y = [FOOD_SIZE*sub for sub in range(int(window_height/FOOD_SIZE))]
print(x,y)
bouncer = {'rect':pygame.Rect(200, 100, 50, 50), 'dir':UPLEFT}
bouncer2 = {'rect':pygame.Rect(200, 100, 50, 50), 'dir':DOWNLEFT}
foods = []
for i in range(20):
    new_square = pygame.Rect(random.choice(x), random.choice(y), FOOD_SIZE, FOOD_SIZE)
    while new_square in foods:
        new_square = pygame.Rect(random.choice(x), random.choice(y), FOOD_SIZE, FOOD_SIZE)
    foods.append(new_square)


# run the game loop
while True:
    # check for the QUIT event
    for event in pygame.event.get():
        if event.type == QUIT:
            print(len(foods))
            pygame.quit()
            sys.exit()

    food_counter += 1

    if food_counter >= NEW_FOOD:
        # add new food
        food_counter = 0
        for i in range(5):
            new_square = pygame.Rect(random.choice(x), random.choice(y), FOOD_SIZE, FOOD_SIZE)
            while new_square in foods:
                new_square = pygame.Rect(random.choice(x), random.choice(y), FOOD_SIZE, FOOD_SIZE)
            foods.append(new_square)



    # draw the black background onto the surface
    window_surface.fill(BLACK)

    # move the bouncer data structure
    if bouncer['dir'] == DOWNLEFT:
        bouncer['rect'].left -= movespeed
        bouncer['rect'].top += movespeed1
    if bouncer['dir'] == DOWNRIGHT:
        bouncer['rect'].left += movespeed
        bouncer['rect'].top += movespeed1
    if bouncer['dir'] == UPLEFT:
        bouncer['rect'].left -= movespeed
        bouncer['rect'].top -= movespeed1
    if bouncer['dir'] == UPRIGHT:
        bouncer['rect'].left += movespeed
        bouncer['rect'].top -= movespeed1


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
       movespeed = random.randint(10,12)
       movespeed1 = random.randint(10,12)

    # draw the bouncer onto the surface
    pygame.draw.rect(window_surface, GREEN, bouncer['rect'])

    # check if the bouncer has intersected with any food squares
    for food in foods:
        if do_rects_overlap(food, bouncer['rect']):
            foods.remove(food)

    # draw the food squares
    for i in range(len(foods)):
        pygame.draw.rect(window_surface, BLUE, foods[i])

    # display update
    pygame.display.update()
    #main_clock.tick(40)
