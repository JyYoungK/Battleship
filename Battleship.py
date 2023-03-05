import random

# Define constants
BOARD_SIZE = 10
NUM_SHIPS = 5
SHIP_LENGTHS = [5, 4, 3, 3, 2]
HORIZONTAL_LABELS = 'ABCDEFGHIJ'
VERTICAL_LABELS = [str(i) for i in range(1, 11)]

# Initialize game variables
gameRunning = True
enemyShipCounts = NUM_SHIPS
myShipPositions = []
computerGuesses = []
hitNumber = 0
gameRound = 1
shipHits = [0 for _ in range(NUM_SHIPS)]

# Define helper functions
def initializeBoard():
    board = []
    for i in range(BOARD_SIZE):
        row = ['-'] * BOARD_SIZE
        board.append(row)

    ships = [(5, 'A'), (4, 'B'), (3, 'C'), (3, 'D'), (2, 'E')]
    for ship_length, col in ships:
        placed = False
        while not placed:
            # Randomly select a starting position for the ship
            row = random.randint(0, BOARD_SIZE - 1)
            start_col = random.randint(0, BOARD_SIZE - ship_length)
            end_col = start_col + ship_length - 1

            # Check if the ship would overlap with an existing ship
            overlap = False
            for c in range(start_col, end_col + 1):
                if board[row][c] != '-':
                    overlap = True
                    break

            if not overlap:
                # Place the ship on the board
                for c in range(start_col, end_col + 1):
                    board[row][c] = col

                # Add the ship positions to myShipPositions
                for c in range(start_col, end_col + 1):
                    myShipPositions.append((row, c))

                placed = True

    return board

def printBoard(board):
    print("  " + " ".join(HORIZONTAL_LABELS))
    for i in range(BOARD_SIZE):
        print(VERTICAL_LABELS[i] + " " + " ".join(board[i]))


def computerMove():
    global gameRound, hitNumber
    global userBoard, gameRunning
    global myShipPositions, shipHits

    print(f"\n\nGame Round {gameRound}:")
    
     # If the computer has hit a ship, target the surrounding area in the next move
    if hitNumber > 0:
        lastHit = computerGuesses[-1]
        row, col = lastHit[0], lastHit[1]
        while True:
            direction = random.choice(['up', 'down', 'left', 'right'])
            if direction == 'up' and row > 0 and (row-1, col) not in computerGuesses:
                row -= 1
                break
            elif direction == 'down' and row < BOARD_SIZE-1 and (row+1, col) not in computerGuesses:
                row += 1
                break
            elif direction == 'left' and col > 0 and (row, col-1) not in computerGuesses:
                col -= 1
                break
            elif direction == 'right' and col < BOARD_SIZE-1 and (row, col+1) not in computerGuesses:
                col += 1
                break
    else:
        # Otherwise, guess a random location
        row, col = random.choice(list(set((i, j) for i in range(BOARD_SIZE) for j in range(BOARD_SIZE)) - set(computerGuesses)))

    computerGuesses.append((row, col))
    if (row, col) in myShipPositions:
        for i, shipPos in enumerate(myShipPositions):
            if (row, col) == shipPos:
                myShipPositions.pop(i)
                userBoard[row][col] = "O"
                print(f"The computer hit one of your ships at {HORIZONTAL_LABELS[col]}{row+1}!")
                hitNumber += 1
                shipHits[i] += 1
                if shipHits[i] == SHIP_LENGTHS[i]:
                    print(f"Ship {SHIP_LABELS[i]} has been sunk!")
                break
        if len(myShipPositions) == 0:
            print("All your ships have been sunk. You lose.")
            gameRunning = False
        elif hitNumber == NUM_SHIPS:
            print("The computer has sunk all your ships. You lose.")
            gameRunning = False
    else:
        userBoard[row][col] = "X"
        print(f"The computer missed at {HORIZONTAL_LABELS[col]}{row+1}!")


# Initialize the game
userBoard = initializeBoard()
print("Game has been initialized")
printBoard(userBoard)

print("\nGame starting")
# Start the game loop
while(gameRunning):
    computerMove()
    printBoard(userBoard)
    gameRound += 1

