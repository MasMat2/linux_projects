# import pygame, sys, random
# from pygame.locals import *
#
# # check if one square is inside the other
# def do_rects_overlap(rect1, rect2):
#     for a, b in [(rect1, rect2), (rect2, rect1)]:
#         # Check if a's corners are inside b
#         if((is_point_inside_rect(a.left, a.top, b)) or
#             (is_point_inside_rect(a.left, a.bottom, b)) or
#             (is_point_inside_rect(a.right, a.top, b)) or
#             (is_point_inside_rect(a.right, a.bottom, b))):
#             return True
#     return False
#
# # check if one point is inside a rect object
# def is_point_inside_rect(x, y, rect):
#     if (x > rect.left) and (x < rect.right) and (y > rect.top) and (y < rect.bottom):
#         return True
#     else:
#         False
#
#
# # set up pygame
# pygame.init()
#
# window_width = 270
# window_height = 180
#
# # set up the window
# window_surface = pygame.display.set_mode((window_width, window_height), 0, 32)
# pygame.display.set_caption('MA Men!')
#
# # set up the colors
# BLACK = (40, 44, 52)
# WHITE =(255, 255, 255)
# GREEN = (150, 253, 109)
# RED = (254, 55, 190)
# BLUE = (87, 199, 208)
# PURPLE = (203, 103, 211)
# RED1 =(242, 15, 61)
# BROWN = (215,168, 142)
# ORANGE = (255, 176, 97)
# YELLOW = (238, 226, 0)
# COLORS = [GREEN, RED, BLUE, PURPLE, RED1, BROWN, ORANGE, YELLOW]
#
# # set up direction variables
# DOWNLEFT = 1
# DOWNRIGHT = 3
# UPLEFT = 7
# UPRIGHT= 9
# DIRECTIONS =[DOWNLEFT, DOWNRIGHT, UPLEFT, UPRIGHT]
#
# # initial speed
# movespeed = 10
# movespeed1 = 10
#
# # set up text
# letters = 'Hsi'
#
# # set square's letter size
# square_width = int(window_width/9)
# square_height = int(window_height/5)
#
# # get the x and y center of the window
# centerx = window_surface.get_rect().centerx
# centery = window_surface.get_rect().centery
#
# # get x and y coordinates for the fisrt square's letter
# letterx = centerx - (square_width/2)*len(letters)
# print(letterx) ##
# lettery = centery - square_height/2
# print(square_width, square_height) ##
#
# # create bouncers
# bouncers = []
# for i in range(5):
#     color = random.choice(COLORS)
#     direction = random.choice(DIRECTIONS)
#     x = random.randint(0,window_width)
#     y = random.randint(0,window_height)
#     side = 2
#     bouncers.append({'rect':pygame.Rect(x, y, random.choice([side]), random.choice([side])), 'dir':direction, 'color':color, 'speed':10, 'speed1':10})
#
#
# # run the game loop
# while True:
#     for event in pygame.event.get():
#         if event.type == QUIT:
#             pygame.quit()
#             sys.exit()
#
#     # draw the white background onto the surface
#     window_surface.fill(WHITE)
#
#     # draw  one suare per letter
#     count = 1
#     for letter in range(len(letters)):
#         lx = letterx + square_width*(count-1)
#         pygame.draw.rect(window_surface, COLORS[count], (lx, lettery, square_width, square_height))
#         count += 1
#
#     pygame.draw.rect(window_surface, BLACK, (centerx, centery, 1, 100))
#
#     # draw bouncers
#     for bouncer in bouncers:
#         # move the bouncer data structure
#         if bouncer['dir'] == DOWNLEFT:
#             bouncer['rect'].left -= movespeed
#             bouncer['rect'].top += movespeed1
#         if bouncer['dir'] == DOWNRIGHT:
#             bouncer['rect'].left += movespeed
#             bouncer['rect'].top += movespeed1
#         if bouncer['dir'] == UPLEFT:
#             bouncer['rect'].left -= movespeed
#             bouncer['rect'].top -= movespeed1
#         if bouncer['dir'] == UPRIGHT:
#             bouncer['rect'].left += movespeed
#             bouncer['rect'].top -= movespeed1
#
#
#         # check if the bouncer has move out the window
#         if bouncer['rect'].top < 0:
#             if bouncer['dir'] == UPLEFT:
#                 bouncer['dir'] = DOWNLEFT
#             if bouncer['dir'] == UPRIGHT:
#                 bouncer['dir'] = DOWNRIGHT
#         if bouncer['rect'].right > window_width: # bug the dir chenged from 3 to 1 for a mistake in the > sign
#             if bouncer['dir'] == UPRIGHT:
#                 bouncer['dir'] = UPLEFT
#             if bouncer['dir'] == DOWNRIGHT:
#                 bouncer['dir'] = DOWNLEFT
#         if bouncer['rect'].bottom > window_height:
#             if bouncer['dir'] == DOWNLEFT:
#                 bouncer['dir'] = UPLEFT
#             if bouncer['dir'] == DOWNRIGHT:
#                 bouncer['dir'] = UPRIGHT
#         if bouncer['rect'].left < 0:
#             if bouncer['dir'] == UPLEFT:
#                 bouncer['dir'] = UPRIGHT
#             if bouncer['dir'] == DOWNLEFT:
#                 bouncer['dir'] = DOWNRIGHT
#         if (bouncer['rect'].top < 0 or bouncer['rect'].right > window_width or
#            bouncer['rect'].bottom > window_height or bouncer['rect'].left < 0):
#            bouncer['speed'] = random.randint(2,20)
#            bouncer['speed'] = random.randint(2,20)
#
#         # draw the bouncer onto the surface
#         pygame.draw.rect(window_surface, bouncer['color'], bouncer['rect'])
#
#
#
#
#
#
#     # draw the window onto the screen
#     pygame.display.update()

for x in range(50):
    print('/////////////////////////////////////////////////////////////////////////')
