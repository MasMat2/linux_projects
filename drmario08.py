import pygame, random, sys, copy
from pygame.locals import   *

WHITE = (255,255,255)
BLACK = (0,0,0)
BLUE = (87, 199, 208)
GREEN = (150, 253, 109)
PURPLE = (203, 103, 211)
ORANGE = (255, 176, 97)
YELLOW = (238, 226, 0)
COLORS = [BLUE,GREEN,YELLOW,PURPLE]


class Window():
    def __init__(self):
        self.caption = "Doctor Mario"
        self.surface = pygame.display.set_mode((768, 384), 0 , 32)

class Player():

    def __init__(self):
        self.speed = 24

        self.color = random.choice(COLORS)
        self.color_tail = random.choice(COLORS)
        self.rect = pygame.Rect(x, 0, 24, 24)
        self.rect_tail = pygame.Rect(x, 0, 24, 24)

        self.move_right = False
        self.move_left = False
        self.move_down = False

        self.right_tail = True
        self.down_tail = False
        self.left_tail = False
        self.up_tail = False



    def move(self):

        if self.move_right:
            player_copy.rect.right += self.speed

        elif self.move_left:
            player_copy.rect.right -= self.speed

        if self.move_down:
            player_copy.rect.bottom += self.speed

        if self.right_tail:
            i, j = self.speed, 0
        elif self.down_tail:
            i, j =  0, self.speed
        elif self.left_tail:
            i, j = -self.speed, 0
        elif self.up_tail:
            i, j = 0, -self.speed

        player_copy.rect_tail.left = player_copy.rect.left + i
        player_copy.rect_tail.top = player_copy.rect.top + j

        # not move player in one second movedown

    def turn(self):

        if self.right_tail:
            self.right_tail = False
            self.down_tail = True
        elif self.down_tail:
            self.down_tail = False
            self.left_tail = True
        elif self.left_tail:
            self.left_tail = False
            self.up_tail = True
        elif self.up_tail:
            self.up_tail = False
            self.right_tail = True


        # right bottom fixed
        return True

    def touch(self):
        front = (player.rect.bottom, player.rect.left) in toplefts
        back  = (player.rect_tail.bottom, player.rect_tail.left) in toplefts
        if front or back:
            toplefts.append((player.rect, player.rect_tail))
            return True

class Player_copy():

    def __init__(self):
        self.color = copy.copy(player.__dict__['color'])
        self.rect = copy.copy(player.__dict__['rect'])
        self.color_tail = copy.copy(player.__dict__['color_tail'])
        self.rect_tail = copy.copy(player.__dict__['rect_tail'])


def valid():
    global h

    top = player_copy.rect.top >= 0 and player_copy.rect_tail.top >= 0
    bottom = player_copy.rect.bottom <= h and player_copy.rect_tail.bottom <= h
    left = player_copy.rect.left >= 0 and player_copy.rect_tail.left >= 0
    right = player_copy.rect.right <= w and player_copy.rect_tail.right <= w

    front_inside = (player_copy.rect.top, player_copy.rect.left) in toplefts
    back_inside = (player_copy.rect_tail.top, player_copy.rect_tail.left) in toplefts

    if top and bottom and left and right:
        if not(front_inside or back_inside):
            return True
    else:
        return False

def update_player():
    global player_copy
    player_copy = Player_copy()
    player.move()
    if valid():
        player.rect = player_copy.rect
        player.rect_tail = player_copy.rect_tail

def update_blocks():
    global blocks, player_copy, player, h, timer

    bottom = player_copy.rect.bottom == h or player_copy.rect_tail.bottom == h
    block_touch = player.touch()

    if (bottom or block_touch) and timer == 0:
        timer = 1
        pygame.time.set_timer(25, 1000)

    if (bottom or block_touch) and timer == 2:
        timer = 0
        toplefts.append((player_copy.rect.top, player_copy.rect.left))
        toplefts.append((player_copy.rect_tail.top, player_copy.rect_tail.left))

        new_block = {}
        block_atrib = ['color', 'color_tail', 'rect', 'rect_tail']
        for atrib in block_atrib:
            new_block[atrib] = player.__dict__[atrib]
        blocks.append(new_block)
        player = Player()
        pygame.time.set_timer(25, 0)
    elif (not (bottom or block_touch)) and timer ==  1:
        timer = 0
        pygame.time.set_timer(25, 0)

def draw_blocks():
    for block in blocks:
        pygame.draw.rect(window.surface, block["color"], block["rect"])
        pygame.draw.rect(window.surface, block["color_tail"], block["rect_tail"])

def draw_player():
    pygame.draw.rect(window.surface, player.color, player.rect)
    pygame.draw.rect(window.surface, player.color_tail, player.rect_tail)

pygame.init()
clock = pygame.time.Clock()
window = Window()
w, h = window.surface.get_size()
x = (w/2) - 24
player = Player()
blocks = []
toplefts = []
timer = 0


while 1:

    clock.tick_busy_loop(8)
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

        if event.type == KEYDOWN:
            if event.key == K_LEFT:
                player.move_right = False
                player.move_left = True
            if event.key == K_RIGHT:
                player.move_right = True
                player.move_left = False
            if event.key == K_DOWN:
                player.move_down = True

        if event.type == KEYUP:
            if event.key == K_ESCAPE:
                pygame.quit()
                sys.exit()
            if event.key == K_LEFT:
                player.move_left = False
            if event.key == K_RIGHT:
                player.move_right = False
            if event.key == K_DOWN:
                player.move_down = False
            if event.key == K_SPACE:
                player.turn()

        if event.type == 25:
            timer = 2

    update_player()
    update_blocks()

    window.surface.fill(BLACK)

    draw_player()
    draw_blocks()

    pygame.display.update()
