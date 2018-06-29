import pygame, random, sys, copy
from pygame.locals import *

# function to move the player down
def moved():
    if top['rect'].top < WINDOWHEIGHT-speed:
        top['rect'].top += speed

# move the player left, right or down
def moveside(a):
    right = moveright and top['rect'].left < WINDOWWIDTH - speed*2
    left = moveleft and top['rect'].left >= speed
    down = movedown and top['rect'].top < WINDOWHEIGHT-speed

    if right:
        top['rect'].left += speed
    if left:
        top['rect'].left -= speed
    if down:
        top['rect'].top += speed
    if down:
        return pygame.time.get_ticks()
    return a

def reversemove():
    for sprite in sprites[:]:
        if insiderect(pix['rect'],sprite['rect']):
            if moveright:
                top['rect'].left -= speed
                tail['rect'].left -= speed
            if moveleft:
                top['rect'].left += speed
                tail['rect'].left += speed
            return True


# check if the player inside any block
def insiderect(player, sprite):
    return (player.bottom, player.left) == (sprite.bottom, sprite.left)

# check if the new position of the player is touching any block
def emptyspace(player, spaces):
    if (player.bottom, player.left) in spaces:
        return False
    return True

# get coordinates used
def newpos(bug):
    if bug not in sprites:
        sprites.append(bug)
    spaces.append((bug['rect'].top, bug['rect'].left))

def playertail():
    (tail['rect'].bottom, tail['rect'].left) = (top['rect'].bottom, top['rect'].right)

def touchsprite():
    for pix in player:
        if not emptyspace(pix['rect'], spaces):
            return True

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

# set up sprites
x = (WINDOWWIDTH/2)
y = 0
top = {"rect":pygame.Rect(x , y, PILLW, PILLH), "dir": moveright, "color":WHITE}
tail = {"rect":pygame.Rect(x , y, PILLW, PILLH), "dir": moveright, "color":WHITE}
player = (top,tail)
sprites = [({"rect":pygame.Rect(144 , 336, PILLW, PILLH), "dir": moveright, "color":BLUE}),({"rect":pygame.Rect(168, 336, PILLW, PILLH), "dir": moveright, "color":BLUE}), ({"rect":pygame.Rect(144 , 360, PILLW, PILLH), "dir": moveright, "color":BLUE}), ({"rect":pygame.Rect(168 , 360, PILLW, PILLH), "dir": moveright, "color":BLUE})]

# check set timer method
a = pygame.time.get_ticks()
b = pygame.time.get_ticks()

# get spaces
spaces = []
for bot in range(0, WINDOWWIDTH, speed):
    spaces.append((WINDOWHEIGHT, bot))

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




    #### MOVE PLAYER

    # Move down every second
    if not movedown and pygame.time.get_ticks() - a > 1000:
        a = pygame.time.get_ticks()
        moved()

    # Update position 10 times per second
    if (pygame.time.get_ticks() - b > 100):
        b = pygame.time.get_ticks()
        a = moveside(a)

    playertail()
    for pix in player:
        if reversemove():
            break


    # Check if new position is touching a sprite
    for pill in sprites[:]:
        if touchsprite():
            topbug = copy.deepcopy(top)
            tailbug = copy.deepcopy(tail)
            if topbug not in sprites:
                newpos(topbug)
                newpos(tailbug)

            # Move player to the original position
            top["rect"] = pygame.Rect(x, y, PILLW, PILLH)
            break


    #### DRAW

    # Surface
    window_surface.fill(BLACK)

    # Sprites
    for pill in sprites:
        pygame.draw.rect(window_surface, pill["color"], pill["rect"])

    # Player
    for pix in player:
        pygame.draw.rect(window_surface, pix["color"], pix["rect"])

    # Update
    pygame.display.update()
