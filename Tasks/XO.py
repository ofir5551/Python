import os

board = [[1, 2, 3],
         [4, 5, 6],
         [7, 8, 9]]

# Prints the board
def printBoard():
    os.system('cls')
    print("-------------")
    for x in range(0,3):
        print("|",board[x][0],"|",board[x][1],"|",board[x][2],"|")
        print("-------------")

# Reset the game board after restarting another game
def resetBoard():
    global board
    board = [[1, 2, 3],
             [4, 5, 6],
             [7, 8, 9]]

# Checks if the player's choice is already taken
def isTaken(choice):
    if choice > 0 and choice < 4:
        if board[0][choice-1] == 'X' or board[0][choice-1] == 'O':
            return True

    if choice > 3 and choice < 7:
        if board[1][choice-4] == 'X' or board[1][choice-4] == 'O':
            return True

    if choice > 6 and choice < 10:
        if board[2][choice-7] == 'X' or board[2][choice-7] == 'O':
            return True

# Places the player's mark on the board
def placeMark(choice, player):
    if choice > 0 and choice < 4:
        board[0][choice-1] = player

    if choice > 3 and choice < 7:
        board[1][choice-4] = player

    if choice > 6 and choice < 10:
        board[2][choice-7] = player

def checkBoard():
    # Checking rows
    for i in range(0, 3):
        if board[i][0] == board[i][1] and board[i][0] == board[i][2]:
            return True

    # Checking columns
    for i in range(0, 3):
        if board[0][i] == board[1][i] and board[0][i] == board[2][i]:
            return True

    # Checking diagonals
    if board[0][0] == board[1][1] and board[0][0] == board[2][2]:
        return True
    if board[2][0] == board[1][1] and board[2][0] == board[0][2]:
        return True

# 2 counters for X wins and O wins
xWins = 0
oWins = 0

print("Welcome to X-O Game!\nThis is your board: \n")

def startGame():
    global xWins, oWins
    resetBoard() 
    printBoard()
    isPlaying = True
    countMoves = 0
    
    while isPlaying:
        if countMoves % 2 == 0:
            player = 'X'
            choice = (int)(input("Player ' X ' enter number: "))
            print("\n")
        else:
            player = 'O'
            choice = (int)(input("Player ' O ' enter number: "))
            print("\n")

        while choice < 1 or choice > 9 or isTaken(choice):  # Checks for invalid player choices
            print("Invalid choice. Player ' " + player + " ' enter number: ")
            choice = (int)(input())
        
        placeMark(choice, player) # Places the player's choice on the board

        printBoard()
        countMoves += 1

        if (checkBoard()):      # Checks if someone has won the game
            isPlaying = False
            if player == 'X':
                xWins += 1
                print("---VICTORY:", player, "HAS WON", xWins, "TIMES---")
            else:
                oWins += 1
                print("---VICTORY:", player, "HAS WON", oWins, "TIMES---")

        if countMoves == 9:
            isPlaying = False
            if not checkBoard():
                print("---DRAW---")

    anotherGame = int(input("Would you like to play another game? Enter 1 for yes, 0 for no: "))
    if anotherGame:
        print("\n")
        startGame()
    else:
        print("---GAME OVER---")
        print("---VICTORY: 'X' HAS WON", xWins, "TIMES---")
        print("---VICTORY: 'O' HAS WON", oWins, "TIMES---")


startGame()