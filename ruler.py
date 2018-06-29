# import pygame
# from pygame.locals import *

widths = [59, 77, 79, 81, 91, 92, 94, 110]
ind = ["h", "f", "g", "c", "d", "a", "b", "e"]
unity = [(300/92), (300/110)]
for un in unity:
    if un == 300/92:
        print("\nUnity {}\n".format("300/92"))
    else:
        print("\nUnity {}\n".format("300/110"))
    for le in widths:
        print("{}({}) = {}".format(le, ind[widths.index(le)], le*un))

#
# # set up pygame
# pygame.init()
# mainclock = pygame.time.Clock()
#
# # set up window
# WINDOWWIDTH = 0
# WINDOWHEIGHT = 0
# window_surface = pygame.display.set_mode((WINDOWWIDTH, WINDOWHEIGHT), 0 , 32)
# pygame.display.set_caption("Doctor Mario")
#
# myimage = pygame.image.load("scene.png")
# imagerect = myimage.get_rect()
# imagerect.center = window_surface.get_rect().center
#
# cor = {}
# count  = 1
# # set game loop
# while True:
#
#     #check fro quit event
#     for event in pygame.event.get():
#         if event.type == QUIT:
#             for key in cor.keys():
#                 print("Click {},   Coor {}".format(key, cor[key]))
#             pygame.quit()
#             sys.exit()
#         if event.type == MOUSEBUTTONDOWN:
#             cor[count] = pygame.mouse.get_pos()
#             count += 1
#
#     window_surface.fill((0,0,0))
#     window_surface.blit(myimage, imagerect)
#     pygame.display.flip()
