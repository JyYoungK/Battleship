import random



def printBoard(board):

    print("      A       B       C       D       E       F       G       H       I       J")

    print()

    for i in range(1, 11):

        if (i == 10):

            print(i, end="    ")

        else:

            print(i, end="     ")

        for j in board[i-1]:

            print(j, end="       ")

        print()

        print()

        print()



def printInstructions():

    print("Welcome to Battleship.")

    print(" ")

    print("Here are the instructions on how to play:")

    print("This is a 2 player game between you and the computer.") 

    print("You will have 5 ships. They will be randomly placed on the game board for you.")

    print("The object of the game is to sink all 5 of your opponent's ships before they sink all of your ships.")

    print("Enter a coordinate (Ex. B4) to guess where your opponent's ships are. Both players will not be able to see each others ships.")

    print ("∅ will be shown if you miss the ship. ⊙ will be shown if you hit your opponent's ship.")

    print("There will be 2 game boards shown. One will be your own with your ships and the other is your opponent's board. However, their ships can not be seen and only your guesses will be shown.")

    print("Good luck. The game will now start.")

    print(" ")



def userMove(computerBoard):

    print ("User Moves")



#Making the dots for the game board

userBoard = []

computerBoard = []



for i in range(10):

    userBoard.append(list("●"*10))

    computerBoard.append(list("●"*10))





def computerMove():

    global hitNumber, gameRound, enemyShipCounts, gameRunning, computerGusses

    

    alphabetChoices = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J']

    numberChoices = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10']

    alphabet = random.choice(alphabetChoices)

    number = int(random.choice(numberChoices))

    

    while [alphabet, number] in computerGuesses:

        alphabet = random.choice(alphabetChoices)

        number = int(random.choice(numberChoices))

        

    computerGuesses.append([alphabet, number])

    print("The computer guessed: ", [alphabet, number])

    

    if [alphabet, number] in myShipPositions:

        print("The computer hit your ship!")

        hitNumber += 1

        x = number - 1

        y = ord(alphabet) - 65

        userBoard[x][y] = "⊙" ## Mark it as hit

        if hitNumber == enemyShipCounts:

            print("Game over! The computer found all your ships in", gameRound, "rounds.")

            gameRunning = False

    else:

        print("The computer missed!")

        x = number - 1

        y = ord(alphabet) - 65

        userBoard[x][y] = "∅" ## Mark it as missed



    





printInstructions()

printBoard(userBoard)

gameRunning = True

enemyShipCounts = 5

myShipPositions = [["G",1],["G",2],["G",3],["G",4],["G",5]] ## Change this to more realistic values

computerGuesses = []



hitNumber = 0

gameRound = 1



while(gameRunning):

    print ("This is Game Round" , gameRound)

    ## userMove()

    computerMove()

    printBoard(userBoard)

    gameRound += 1