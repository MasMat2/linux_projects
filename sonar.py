# Sonar

import random, sys

def draw_board(board):
    # Draw the board data stucture.

    hline = '   ' # initial space for the numbers down the left side of the board.
    for i in range(1, 6):
        hline += (' ' * 9) + str(i)

    # print the numbers across the top.
    print(hline)
    print('  ' + ('0123456789' * 6))
    print()

    # print each of the 15 rows.
    for i in range(15):
        # single-digit numbers need to be paddded with an extra space.
        if i < 10:
            extra_space = ' '
        else:
            extra_space = ''
        print('%s%s%s%s' % (extra_space, i, get_row(board, i),i))

    # print the numbers across the bottom.
    print()
    print('  ' + ('0123456789' * 6))
    print(hline)


def get_row(board, row):
    # Return a string from the board data structure at a certain row.
    board_row = ''
    for i in range(60):
        board_row += board[i][row]
    return board_row

def get_new_board():
    # Create a new 60x15 board data structure.
    board = []
    for x in range(60): # the main list is a list of 60 lists
            board.append([])
            for y in range(15): # each list in the main list has 15 single-character strings
            # use different characters for the ocean to make it more readable
                if random.randint(0,1) == 0:
                    board[x].append('~')
                else:
                    board[x].append('`')
    return board

def get_random_chests(num_chests):
    # Create a list of chest data structures (two-item lists of x, y int coordinates)
    chests = []
    for i in range(num_chests):
        while True:
            new = ([random.randint(0, 59), random.randint(0, 14)])
            if new not in chests:
                chests.append(new)
                break

    print(chests)
    return chests

def is_valid_move(x, y):
    # Return True if the coordinates are on the board, otherwise False.
    return x >= 0 and x <= 59 and y >= 0 and y <= 14

def make_move(board, chests, x , y):
    # Change the board data structure with a sonar device character. Remove treasure chests
    # form the chests list as they are found. Return False if this is an invalid move.
    # Otherwise, return the string of the result of this move.
    if not is_valid_move(x, y):
        return False

    smallest_distance = 100 # any chest will be closer than 100.
    for cx, cy in chests:
        if abs(cx - x) > abs(cy - y):
            distance = abs(cx - x)
        else:
            distance = abs(cy - y)

        if distance < smallest_distance: # we want the closest treasure chest.
            smallest_distance = distance

    if smallest_distance == 0:
        # xy is directly on a treasure ches!
        chests.remove([x,y])
        return "You have found a sunken treasure chest!"
    else:
        if smallest_distance < 10:
            board[x][y] = str(smallest_distance)
            return "Treasure detected at a distance of %s form the sonar device." % (smallest_distance)
        else:
            board[x][y] = 'O'
            return 'Sonar did not detect anything. All treasure chests out of range.'


def enter_player_move():
    # Let the player type in their move. Return a two-item list of int xy coordinates.
    print('Where do you want to drop the next sonar device? (0-59 0-14) (or type quit)')
    while True:
        move = input()
        if move.lower() == 'quit':
            print('Thanks for playing!')
            sys.exit()

        move = move.split()
        if len(move) == 2 and move[0].isdigit() and move[1].isdigit() and is_valid_move(int(move[0]), int(move[1])):
            if [int(move[0]), int(move[1])] not in previous_moves:
                return [int(move[0]), int(move[1])]
            print('Please enter a new number')
            continue
        print('Enter a number from 0 to 59, a space, then a number from 0 to 14.')


def play_again():
    # This function returns True if the player wants to play again, otherwise it return False.
    print('Do you want to play again? (yes or no)')
    return input().lower().startswith('y')


def show_instructions():
    print('''Instructions:
You are the captain of the Simon, aa treasure-hunting ship. Your current mission
is to find the three sunken treasure chests that are lurking in the part of the
ocean you are in and collect them.

To play, enter the coordinates of the point in the ocean you wish to drop a
sonar device. The sonar can find out how far away the closest chest is to it.
For example, the d below marks where the device was dropped, and the 2's
represent distances of 2 away form the device. The 4's represent
distance of 4 away from the device.
''')
    input()

    print('''For example, here is a treasure chest (the c) located a distance of 2 away
from the soanr device (the d):

The point where the device was dropped will be marked with a 2.

The treasure chests don't move around. Sonar devices can detect treasure
chests up to a distance of 9. If all chests are out of range, the point
will be marked with O

If a device is directly dropped on a treasure chest, you have discovered
the location of the chest, and it will be collected. The sonar device will
remain there.

When You collect a chest, all sonar devices will update to lacate the next
closest sunken treasure chest.
Pleas enter to continue...''')
    input()
    print()


print('S O N A R!')
print()
print('Would you like to view the instructions? (yes/no)')
if input().lower().startswith('y'):
    show_instructions()

while True:
    # game setup
    sonar_devices = 16
    the_board = get_new_board()
    the_chests = get_random_chests(3)
    draw_board(the_board)
    previous_moves = []

    while sonar_devices > 0:
        # Start of a turn:

        # show saonar device/chest status
        if sonar_devices > 1: extra_Ssonar = 's'
        else: extra_Ssonar = ''
        if len(the_chests) > 1: extra_Schest = 's'
        else: extra_Schest = ''
        print('You have %s sonar devices%s left. %s treasure chest%s remaining.' % (sonar_devices, extra_Ssonar, len(the_chests), extra_Schest))

        x, y = enter_player_move()
        previous_moves.append([x, y]) # we must track all moves so that sonar devices can be updated.

        move_result = make_move(the_board, the_chests, x, y)
        if move_result == False:
            continue
        else:
            if move_result == 'You have found a sunken treasure chest!':
                # update all the sonar devices currently on the map.
                for x, y in previous_moves:
                    make_move(the_board, the_chests, x, y)
            draw_board(the_board)
            print(move_result)

        if len(the_chests) == 0:
            print('You have found all the sunken treasure chests! Congatulations and good game!')
            break

        sonar_devices -= 1

    if sonar_devices == 0:
        print('We\'ve run out of sonar devices! Now we have to turn the ship around and head')
        print('for home with treasure chests still out there! Game over.')
        print('  The remaining chests were here:')
        for c, y in the_chests:
            print('  %s, %s' % (x,y))

    if not play_again():
        sys.exit()
