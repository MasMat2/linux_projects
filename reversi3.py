# Reversi

import random, time
import sys


def drawBoard(board):
    # This function prints out the board that it was passed. Returns None.
    HLINE = '  +' +'---+'*8
    VLINE = '  |   |   |   |   |   |   |   |   |'

    print(' '+'   1   2   3   4   5   6   7   8')
    print(HLINE)
    print(VLINE)
    for y in range(8):
        print(' %s' % (y+1), end='')
        for x in range(8):
            print('| %s'  % (board[x][y]), end=' ')
        print('|')
        print(VLINE)
        print(HLINE)


def resetBoard(board):
    # Blanks out the board it is passed, except for the original starting position.
    for x in range(8):
        for y in range(8):
            board[x][y] = ' '

    # Starting pieces:
    board[3][3] = 'X'
    board[3][4] = 'O'
    board[4][3] = 'O'
    board[4][4] = 'X'


def getNewBoard():
    # Creates a brand new, blank board data structure.
    board = []
    for i in range(8):
        board.append([' '] * 8)

    return board


def isValidMove(board, tile, xstart, ystart):
    # Returns False if the player's move on space xstart, ystart is invalid.
    # If it is a valid move, returns a list of spaces that would become the player's if they made a move here.
    if board[xstart][ystart] != ' ' or not isOnBoard(xstart, ystart):
        return False

    board[xstart][ystart] = tile # temporarily set the tile on the board.

    if tile == 'X':
        otherTile = 'O'
    else:
        otherTile = 'X'

    tilesToFlip = []
    for xdirection, ydirection in [[0, 1], [1, 1], [1, 0], [1, -1], [0, -1], [-1, -1], [-1, 0], [-1, 1]]:
        x, y = xstart, ystart
        x += xdirection # first step in the direction
        y += ydirection # first step in the direction
        if isOnBoard(x, y) and board[x][y] == otherTile:
            # There is a piece belonging to the other player next to our piece.
            x += xdirection
            y += ydirection
            if not isOnBoard(x, y):
                continue
            while board[x][y] == otherTile:
                x += xdirection
                y += ydirection
                if not isOnBoard(x, y): # break out of while loop, then continue in for loop
                    break
            if not isOnBoard(x, y):
                continue
            if board[x][y] == tile:
                # There are pieces to flip over. Go in the reverse direction until we reach the original space, noting all the tiles along the way.
                while True:
                    x -= xdirection
                    y -= ydirection
                    if x == xstart and y == ystart:
                        break
                    tilesToFlip.append([x, y])

    board[xstart][ystart] = ' ' # restore the empty space
    if len(tilesToFlip) == 0: # If no tiles were flipped, this is not a valid move.
        return False
    return tilesToFlip


def isOnBoard(x, y):
    # Returns True if the coordinates are located on the board.
    return x >= 0 and x <= 7 and y >= 0 and y <=7


def getBoardWithValidMoves(board, tile):
    # Returns a new board with . marking the valid moves the given player can make.
    dupeBoard = getBoardCopy(board)

    for x, y in getValidMoves(dupeBoard, tile):
        dupeBoard[x][y] = '.'
    return dupeBoard


def getValidMoves(board, tile):
    # Returns a list of [x,y] lists of valid moves for the given player on the given board.
    validMoves = []

    for x in range(8):
        for y in range(8):
            if isValidMove(board, tile, x, y) != False:
                validMoves.append([x, y])
    return validMoves


def getScoreOfBoard(board):
    # Determine the score by counting the tiles. Returns a dictionary with keys 'X' and 'O'.
    xscore = 0
    oscore = 0
    for x in range(8):
        for y in range(8):
            if board[x][y] == 'X':
                xscore += 1
            if board[x][y] == 'O':
                oscore += 1
    return {'X':xscore, 'O':oscore}


def enterPlayerTile():
    # Lets the player type which tile they want to be.
    # Returns a list with the player's tile as the first item, and the computer's tile as the second.
    tile = ''
    while not (tile == 'X' or tile == 'O'):
        print('Do you want to be X or O?')
        tile = input().upper()

    # the first element in the tuple is the player's tile, the second is the computer's tile.
    if tile == 'X':
        return ['X', 'O']
    else:
        return ['O', 'X']


def whoGoesFirst():
    # Randomly choose the player who goes first.
    if random.randint(0, 1) == 0:
        return 'computer'
    else:
        return 'player'


def playAgain():
    # This function returns True if the player wants to play again, otherwise it returns False.
    print('Do you want to play again? (yes or no)')
    return input().lower().startswith('y')


def makeMove(board, tile, xstart, ystart):
    # Place the tile on the board at xstart, ystart, and flip any of the opponent's pieces.
    # Returns False if this is an invalid move, True if it is valid.
    tilesToFlip = isValidMove(board, tile, xstart, ystart)

    if tilesToFlip == False:
        return False

    board[xstart][ystart] = tile
    for x, y in tilesToFlip:
        board[x][y] = tile
    return True


def getBoardCopy(board):
    # Make a duplicate of the board list and return the duplicate.
    dupeBoard = getNewBoard()

    for x in range(8):
        for y in range(8):
            dupeBoard[x][y] = board[x][y]

    return dupeBoard


def isOnCorner(x, y):
    # Returns True if the position is in one of the four corners.
    return (x == 0 and y == 0) or (x == 7 and y == 0) or (x == 0 and y == 7) or (x == 7 and y == 7)


def getPlayerMove(board, playerTile):
    # Let the player type in their move.
    # Returns the move as [x, y] (or returns the strings 'hints' or 'quit')
    DIGITS1TO8 = '1 2 3 4 5 6 7 8'.split()
    while True:
        #print('Enter your move, or type quit to end the game, or hints to turn off/on hints.')
        move = 1
        if move == 'quit':
            return 'quit'
        if move == 'hints':
            return 'hints'

        if move:
            return getComputerMove(board, playerTile)


def getComputerMove(board, computerTile):
    # Given a board and the computer's tile, determine where to
    # move and return that move as a [x, y] list.
    possibleMoves = getValidMoves(board, computerTile)

    # randomize the order of the possible moves
    random.shuffle(possibleMoves)

    # Go through all the possible moves and remember the best scoring move
    bestScore = -1
    for x, y in possibleMoves:
        dupeBoard = getBoardCopy(board)
        makeMove(dupeBoard, computerTile, x, y)
        score = getScoreOfBoard(dupeBoard)[computerTile]
        if score > bestScore:
            bestMove = [x, y]
            bestScore = score
    return bestMove

def getWorstMove(board, computerTile):
    # Given a board and the computer's tile, determine where to
    # move and return that move as a [x, y] list.
    possibleMoves = getValidMoves(board, computerTile)

    # randomize the order of the possible moves
    random.shuffle(possibleMoves)


    # Go through all the possible moves and remember the best scoring move
    worstScore = 65
    for x, y in possibleMoves:
        dupeBoard = getBoardCopy(board)
        makeMove(dupeBoard, computerTile, x, y)
        score = getScoreOfBoard(dupeBoard)[computerTile]
        if score < worstScore:
            worstMove = [x, y]
            worstScore = score
    return worstMove

def cornerBestMove(board, computerTile):
    possibleMoves = getValidMoves(board, computerTile)

    random.shuffle(possibleMoves)

    for x, y in possibleMoves:
        if isOnCorner(x, y):
            return [x, y]

    return getComputerMove(board, computerTile)

def sideCornerBestMove(board, computerTile):
    possibleMoves = getValidMoves(board, computerTile)

    random.shuffle(possibleMoves)

    sideMoves = []
    for x, y in possibleMoves:
        if (x == 0) or (y == 7):
            sideMoves.append([x, y])

    bestScore = -1
    for x, y in sideMoves:
        dupeBoard = getBoardCopy(board)
        makeMove(dupeBoard, computerTile, x, y)
        score = getScoreOfBoard(dupeBoard)[computerTile]
        if score > bestScore:
            bestMove = [x,y]
            bestScore = score
    if bestScore != -1:
        return bestMove

    return cornerBestMove(board, computerTile)





def showPoints(playerTile, computerTile):
    # Prints out the current score.
    scores = getScoreOfBoard(mainBoard)
    print('You have %s points. The computer has %s points.' % (scores[playerTile], scores[computerTile]))



def Strategies(fun, fun2):

    points = 0
    games = 100
    xscore, yscore, tie = 0, 0, 0
    playerTile, computerTile = "X", "O"
    showHints = False
    turn = 'player'

    while points < games:
        # Reset the board and game.
        mainBoard = getNewBoard()
        resetBoard(mainBoard)

        while True:
            if turn == 'player':
                x,y = fun(mainBoard,playerTile)
                makeMove(mainBoard, playerTile, x, y)

                if getValidMoves(mainBoard, computerTile) == []:
                    break
                else:
                    turn = 'computer'

            else:
                x, y = fun2(mainBoard,computerTile)
                makeMove(mainBoard, computerTile, x, y)

                if getValidMoves(mainBoard, playerTile) == []:
                    break
                else:
                    turn = 'player'


        scores = getScoreOfBoard(mainBoard)
        points += 1


        #Add a point to the winner
        if scores['X'] > scores['O']:
            xscore += 1
        elif scores['X'] < scores['O']:
            yscore += 1
        else:
            tie += 1


    xp = round(xscore/games,2)
    yp = round(yscore/games,2)
    tp = round(tie/games,2)
    print('Xscore: %s \nYscore: %s\nTies: %s' % (xscore, yscore, tie))
    print('X =  %s   Y = %s  Tie = %s' % ((xp), (yp), (tp)))


def choice(board, tile):
    return random.choice(getValidMoves(board, tile))


print()
print('Worst vs Best')
Strategies(getWorstMove, getComputerMove )

print()
print('Random vs Best')
Strategies(choice, getComputerMove)

print()
print('Best vs Best')
Strategies(getComputerMove, getComputerMove )

print()
print('SideCornerBest vs Best')
Strategies(sideCornerBestMove, getComputerMove)

print()
print('CornerBest vs Best')
Strategies(cornerBestMove, getComputerMove)
