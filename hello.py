import pygame, sys
from pygame.locals import *

# set up pygame
pygame.init()

# set up the window
windowSurface = pygame.display.set_mode((1080, 720), 0, 32)
pygame.display.set_caption('MA Men!')

# set up the colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (254, 55, 190)
RW = (254, 105, 206)
GREEN =(150, 253, 109)
BLUE = (87, 199, 208)

#set up fonts
basicFont = pygame.font.SysFont(None, 100)

# set up text
text = basicFont.render('HELLO WORLD!', True, WHITE, RW)
textRect = text.get_rect()
print(textRect)
print(textRect.centery)
textRect.centerx = windowSurface.get_rect().centerx
textRect.centery = windowSurface.get_rect().centery
print(textRect.centery)

# draw the white background onto the surface
windowSurface.fill(WHITE)

# draw a green polygon onto the surface
pygame.draw.polygon(windowSurface, GREEN, ((146, 0), (236, 277) , (56, 277), (0, 106)))

# draw some blue lines onto the surface
pygame.draw.line(windowSurface, BLUE, (60, 60), (120, 60), 4)
pygame.draw.line(windowSurface, BLUE, (120, 60), (60, 120))
pygame.draw.line(windowSurface, BLUE, (60, 120), (120, 120), 4)

# draw a blue cicrcle onto the surface
pygame.draw.circle(windowSurface,BLUE, (350, 100), 40, 0)

# draw a red ellipse onto he surface     first pair of points are reference to the second pair
pygame.draw.ellipse(windowSurface, RED, (300, 250, 40, 80), 1 )

# draw the text's background rectangle onto the surface
pygame.draw.rect(windowSurface, RED, (textRect.left - 20, textRect.top - 20, textRect.width + 40, textRect.height + 40))

# get a pixel array of the surface
pixArray = pygame.PixelArray(windowSurface)
pixArray[400][380] = GREEN
del pixArray

# draw the text onto the surface
windowSurface.blit(text, textRect)

pygame.draw.line(windowSurface, BLACK, (0, 0), (500, 400))
pygame.draw.line(windowSurface, BLACK, (500, 0), (0, 400))
pygame.draw.line(windowSurface, BLACK, (399, 379), (0, 0))

# draw the window onto the screen
pygame.display.update()

# run the game loop
while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
