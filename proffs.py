# import pygame, copy
#
#
# class first():
#     def __init__(self):
#         self.rect = pygame.Rect(0,0,24,24)
#
#     def move(self):
#         prof.rect.top += 6
#
# class cop():
#     def __init__(self):
#         self.rect = test.__dict__['rect']
#
#
# test = first()
# prof = cop()
#
# def update_player():
#     prof = cop()
#     test.move()
#
# test.move()
# print(test.rect)

# for i in range(10):
#     update_player()
#     print(test.rect)

# blocks = []
# for i in range(0, 240, 24):
#         blocks.append(i)
#
#
# more = False
# less = False
# count = 1
# portion = (1/(2**count))
#
# def sort():
#     global more, less, count, b, portion
#
#     if less:
#         portion -= (1/(2**count))
#     elif more:
#         portion += (1/(2**count))
#
#     count += 1
#
#     mid = int(portion*len(blocks))
#
#     if blocks[mid] == b:
#         print(True)
#
#     elif b < blocks[mid]:
#         more = False
#         less = True
#         sort()
#
#     elif b > blocks[mid]:
#         more = True
#         less = False
#         sort()
#
# sort()

import pygame
def a():
    print("a")

# set up pygame
pygame.init()
mainclock = pygame.time.Clock()

t = 1000
pygame.time.set_timer(25, t)

while True:

    for event in pygame.event.get():

        if event.type == 25:
            if t == 2000:
                t = 0
                pygame.time.set_timer(25, t)

            else:
                if t != 0:
                    t += 1000
                pygame.time.set_timer(25, t)

            # pygame.time.set_timer(impa, 1000)
            # pygame.time.set_timer(impa, 0)
            a()

# import random
#
# a, b, c, d = 1, 3, 7, 15
#
# abc = [a,b,c,d]
# tup = []
# while len(tup) < 10001:
#     tup.append((random.choice(abc), random.choice(abc)))
#
# rep = {}
# for li in tup:
#     new = li[0] + li[1]
#     if new in rep.keys():
#         rep[new] += 1
#     else:
#         rep[new] = 1
#
# for k in sorted(rep.keys()):
#     print(k, rep[k])
