import pygame, random, sys, copy
from pygame.locals import *

def moved():
    if player['rect'].top < WINDOWHEIGHT-speed:
        player['rect'].top += speed
def moveside(a):
    if moveright and player['rect'].left < WINDOWWIDTH - speed*2:
        player['rect'].left += speed
    if moveleft and player['rect'].left >= speed:
        player['rect'].left -= speed
    if movedown and player['rect'].top < WINDOWHEIGHT-speed:
        player['rect'].top += speed
    for sprite in sprites[:]:
        if insiderect(player['rect'],sprite['rect']):
            if moveright:
                player['rect'].left -= speed
            if moveleft:
                player['rect'].left += speed
            break
    if movedown and player['rect'].top < WINDOWHEIGHT-speed:
        return pygame.time.get_ticks()
    return a


def insiderect(player, sprite):
    print((player.bottom, player.left),(sprite.bottom, sprite.left))
    if (player.bottom, player.left) == (sprite.bottom, sprite.left):
        print("afadfda")
        return True
    else:
        return False

def emptyspace(player, spaces):
    if (player.bottom, player.left) in spaces:
        return False
    return True

def newpos(bug):
    spaces.append((bug['rect'].top, bug['rect'].left))

# set up pygame
pygame.init()
mainclock = pygame.time.Clock()

# set up window
WINDOWWIDTH = 768
WINDOWHEIGHT = 384
window_surface = pygame.display.set_mode((WINDOWWIDTH, WINDOWHEIGHT), 0 , 32)
pygame.display.set_caption("Doctor Mario")

# set up the colors
WHITE = (255,255,255)
BLACK = (0,0,0)
BLUE = (87, 199, 208)
GREEN = (150, 253, 109)
PURPLE = (203, 103, 211)
ORANGE = (255, 176, 97)
YELLOW = (238, 226, 0)

#speed
speed = 24

# set directions
movedown = False
moveright = False
moveleft = False

PILLW = speed
PILLH = speed
x = random.randrange(0, WINDOWWIDTH,   24)

print(x)
y = 0
player = {"rect":pygame.Rect(x , y, PILLW, PILLH), "dir": moveright, "color":WHITE}
sprites = [({"rect":pygame.Rect(144 , 336, PILLW, PILLH), "dir": moveright, "color":BLUE}),({"rect":pygame.Rect(168, 336, PILLW, PILLH), "dir": moveright, "color":BLUE}), ({"rect":pygame.Rect(144 , 360, PILLW, PILLH), "dir": moveright, "color":BLUE}), ({"rect":pygame.Rect(168 , 360, PILLW, PILLH), "dir": moveright, "color":BLUE})]

# check set timer method
a = pygame.time.get_ticks()
b = pygame.time.get_ticks()

# March 28
spaces = []
for x in range(0, WINDOWWIDTH, speed):
    spaces.append((WINDOWHEIGHT, x))
for sprite in sprites:
    newpos(sprite)

# set game loop
while True:
    #check fro quit event
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

        # get player input
        if event.type == KEYDOWN:

            # Keyboard variables
            if event.key == K_LEFT:
                moveright = False
                moveleft = True
            if event.key == K_RIGHT:
                moveright = True
                moveleft = False
            if event.key == K_DOWN:
                movedown = True

        if event.type == KEYUP:
            if event.key == K_ESCAPE:
                pygame.quit()
                sys.exit()
            if event.key == K_LEFT:
                moveleft = False
            if event.key == K_RIGHT:
                moveright = False
            if event.key == K_DOWN:
                movedown = False

    if not movedown and pygame.time.get_ticks() - a > 1000:
        print(pygame.time.get_ticks() - a)
        a = pygame.time.get_ticks()
        moved()
    if (pygame.time.get_ticks() - b > 100):
        b = pygame.time.get_ticks()
        a = moveside(a)


    window_surface.fill(BLACK)


    for pill in sprites[:]:
        if not emptyspace(player['rect'], spaces):
            bug = copy.deepcopy(player)
            if bug not in sprites:
                sprites.append(bug)
                newpos(bug)

            player["rect"] = pygame.Rect(x, y, PILLW, PILLH)

    for pill in sprites:
        pygame.draw.rect(window_surface, pill["color"], pill["rect"])
    #pygame.draw.rect(window_surface, sprite["color"], sprite["rect"])
    pygame.draw.rect(window_surface, player["color"], player["rect"])


    pygame.display.update()
