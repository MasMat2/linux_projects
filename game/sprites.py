import pygame, sys, time, random
from pygame.locals import *

# Set up pygame.
pygame.init()
mainClock = pygame.time.Clock()
print(mainClock)

# Set up the window.
WINDOWWIDTH = 768
WINDOWHEIGHT = 384
windowSurface = pygame.display.set_mode((WINDOWWIDTH, WINDOWHEIGHT), 0, 32)
pygame.display.set_caption('Adventure and time')

# Set up the colors.
WHITE = (255, 255, 255)
BLACK = (0,0,0)

# Set up the block data structure.
back = pygame.Rect(0, 0, 768, 384)
backImage = pygame.image.load('back.jpg')

# Set up the player
player = pygame.Rect(-40, 0, 87, 126)

# Set up the enemies
foodImage = pygame.image.load('jake2.png')
foodStretchedImage = pygame.transform.scale(foodImage, (80, 60))
foods = []
for i in range(1):
    foods.append(pygame.Rect(WINDOWWIDTH +20 , WINDOWHEIGHT-60, 80, 60))

foodCounter = 0
NEWFOOD = 40

# Set up keyboard variables.
moveLeft = False
moveRight = False
moveUp = False
moveDown = False

MOVESPEED = 4

# Abilitate limited jump
jumping = False
jump = False

loop = 0
moving = False
op = player.left
# Run the game loop.
while True:

    frame = str(loop) + 'fff.png'
    playerImage = pygame.image.load(str(frame))


    newframe = op - player.left
    #if the layer moved more than 12 pixels change frame

    if moving and (newframe % 20 > 12):
        loop += 1
    if loop == 8:
        loop = 0
    elif not moving:
        loop = 4

    # Check for the QUIT event.
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

        #-------------------------------------------
        # Get any input from the user
        if event.type == KEYDOWN:
            # Change the keyboard variables.
            if event.key == K_LEFT or event.key == K_a:
                moveRight = False
                moveLeft = True
            if event.key == K_RIGHT or event.key == K_d:
                moveLeft = False
                moveRight = True
                moving = True
            if (event.key == K_UP or event.key == K_w) and jump:
                jump = False
                jumping = True
            if event.key == K_DOWN or event.key == K_s:
                moveUp = False
                moveDown = True

        if event.type == KEYUP:
            if event.key == K_ESCAPE:
                pygame.quit()
                sys.exit()
            if event.key == K_LEFT or event.key == K_a:
                moveLeft = False
            if event.key == K_RIGHT or event.key == K_d:
                moveRight = False
                moving = False
            if event.key == K_UP or event.key == K_w:
                moveUp = False
            if event.key == K_DOWN or event.key == K_s:
                moveDown = False
            if event.key == K_x:
                player.top = random.randint(0, WINDOWHEIGHT - player.height)
                player.left = random.randint(0, WINDOWWIDTH - player.width)
            if event.key == K_m:
                if musicPlaying:
                    pygame.mixer.music.stop()
                else:
                    pygame.mixer.music.play(-1, 0.0)
                musicPlaying = not musicPlaying


    #---------------------------------------------------
    # Set jumping variables
    if jumping:
        moveUp = True
        moveDown = False
    if player.top < 160:
        jumping = False
        moveUp = False
        moveDown = True

    # Move the player.
    if moveDown and player.bottom < WINDOWHEIGHT:
        player.top += MOVESPEED
    if player.bottom == 382:
        jump = True
    if jumping:
        player.top -= MOVESPEED
    if moveLeft and player.left > 0:
        player.left -= MOVESPEED
    if moveRight and player.right < WINDOWWIDTH:
        player.right += MOVESPEED


    #--------------------------------------------------------
    # Draw the white background onto the surface.
    windowSurface.fill(BLACK)
    windowSurface.blit(backImage, back)

    # Draw the block onto the surface.
    windowSurface.blit(playerImage, player)

    # Check whether the block has intersected with any food squares.
    for food in foods[:]:
        if food.colliderect(player):
            foods.remove(food)
            # player = pygame.Rect(player.left, player.top, player.width + 2, player.height + 2)
            # playerStretchedImage = pygame.transform.scale(playerImage, (player.width, player.height))

    # Draw the food.
    for food in foods:
        food.left -= 2
        windowSurface.blit(foodStretchedImage, food)

    # Draw the window onto the screen.
    pygame.display.update()
    mainClock.tick(40)
