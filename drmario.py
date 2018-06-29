import pygame, random, sys, copy
from pygame.locals import *

def moved():
    if player['rect'].top < WINDOWHEIGHT-speed:
        player['rect'].top += speed
def moveside():
    if movedown and player['rect'].top < WINDOWHEIGHT-speed:
        player['rect'].top += speed
    if moveright and player['rect'].left < WINDOWWIDTH - speed*2:
        player['rect'].left += speed
    if moveleft and player['rect'].left >= speed:
        player['rect'].left -= speed

def insiderect(player, sprite):
    bottom = player.bottom >= sprite.top and player.bottom <= sprite.bottom
    right = player.right <= sprite.right and player.right >= sprite.left
    left =  player.left >= sprite.left and player.left <= sprite.right
    top = player.top >= sprite.top and player.top <= sprite.bottom

    if bottom and left:
        return True
    elif bottom and right:
        return True
    else:
        return False
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

#speed
speed = 24

# set directions
movedown = False
moveright = False
moveleft = False

PILLW = speed*2
PILLH = speed
x = random.randrange(0, WINDOWWIDTH,   24)

print(x)
y = 0
player = ({"rect":pygame.Rect(x , y, PILLW, PILLH), "dir": moveright, "color":WHITE})
sprites = [({"rect":pygame.Rect(144 , 336, PILLW, PILLH*2), "dir": moveright, "color":BLUE})]
# check set timer method
a = pygame.time.get_ticks()
b = pygame.time.get_ticks()

# set game loop
while True:
    #x = random.randint(0, WINDOWWIDTH)
    #y =
    #check fro quit event
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        # get player input
        if event.type == KEYDOWN:

            # Keyboard varibles
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
        a = pygame.time.get_ticks()
        moved()
    if pygame.time.get_ticks() - b > 100:
        b = pygame.time.get_ticks()
        moveside()

    window_surface.fill(BLACK)

    for pill in sprites[:]:
        if insiderect(player["rect"], pill["rect"]):
            bug = copy.deepcopy(player)
            if bug not in sprites:
                sprites.append(bug)
            player["rect"] = pygame.Rect(x , y, PILLW, PILLH)
            print(sprites)
    for pill in sprites:
        pygame.draw.rect(window_surface, pill["color"], pill["rect"])
    #pygame.draw.rect(window_surface, sprite["color"], sprite["rect"])
    pygame.draw.rect(window_surface, player["color"], player["rect"])


    pygame.display.update()
