import random

board = list(" "*10)

def draw(board):
        print("  " + board[1] + "|" + "  " + board[2]+ "|" + "  " + board[3])
        print("___|___|___")
        print("  " + board[4] + "|" +"  " + board[5] + "|" + "  " + board[6])
        print("___|___|___")
        print("  " + board[7] + "|" + "  " + board[8] + "|" + "  " + board[9])
        print("   |   |   ")

def space_free(guess):
    if board[int(guess)] == " ":
        return True
    else:
        return False

def choose():
    char = ""
    while (char not in "xo") or (char == "") :
        char = str(input("What do you choose? (X,O)")).lower()
    if char == "x":
        return char, "o"
    else:
        return char, "x"

def first():
    if random.randint(1,2) == 1:
        print("You are the first player")
        return True
    else:
        print("Computer choose first")
        return False

def again():
    again = " "
    while again not in ["y", "n"]:
         again = str(input("Do you want to play again? (y,n)"))
         print(again)
    if again == "y":
        return True
    else:
        return False

def winner(board, computer, op):

    if computer == "x":
        player = "o"
    else:
        player = "x"


    win = [123,456,789,147,258,369,159,357]
    for line in win:
        count = 0
        for space in str(line):
            if board[int(space)] == computer:
                count += 1
            elif board[int(space)] == player:
                count = -1
            else:
                n = int(space)

        if count == op:
            return True, n
    else:
        return False, False

def computer_guess(board, computer):
    if computer == "x":
        player = "o"
    else:
        player = "x"
    blanks = []
    ex, space = winner(board, player, 2)
    ex1, space1 = winner(board, computer, 2)

    if  ex1:
        return  space1

    if  ex:
        return  space
    corners = []
    for space in "1379":
        if board[int(space)] == " ":
            corners.append(int(space))
            return random.choice(corners)

    for space in "123456789":
        if board[int(space)] == " ":
            blanks.append(int(space))
    return random.choice(blanks)

player, computer = choose()
first1 = first()

while True:
    draw(board)

    if first1:
        guess = " "
        while guess not in "123456789" or guess == "":
            guess = input("Take a guess (1-9)")
        if space_free(guess):
            board[int(guess)] = player
        else:
            continue
        first1 = False

    elif not first1:
        guess = computer_guess(board, computer)
        board[guess] = computer
        first1 = True

    if winner(board, computer, 3)[0]:
        draw(board)
        print("Machines won")
        if again():
            player, computer = choose()
            first1 = first()
            board = list(" "*10)
            continue
        else:
            break
    if winner(board, player, 3)[0]:
        draw(board)
        print("Winner")
        if again():
            player, computer = choose()
            first1 = first()
            board = list(" "*10)
            continue
        else:
            break
    if " " not in board[1:]:
        if again():
            player, computer = choose()
            first1 = first()
            board = list(" "*10)
            continue
        else:
            break
