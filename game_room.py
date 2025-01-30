
#Coin Toss

'''import random
tails = 0
heads = 0

for i in range (0,100,1):
    flip = random.randint(0,1)
    if flip == 0:
        heads += 1
    else:
        tails += 1
print("Number of heads = " + str(heads))
print("Number of tails = " + str(tails))'''

#========================================================================================================
#game menu

import random
play = "y"

def hangman():
    points = 0

    #dict = {"name": "Katherine","Title": "student"}
    #for each in dict:
        #print(dict)
    #constants
    words = ("overused", "clam", "guam", "end of semester", "prom", "homework", "pickle", "enterprise", "xylophone", "zebra")

    hangman = (

        """
        -------
        |     |
        |     |
        |
        |
        |
        |
        |
        |
        |
        |
        |
        -----------""",
        """
        -------
        |     |
        |     |
        |     O
        |
        |
        |
        |
        |
        |
        |
        |
        -----------""",
        """
        -------
        |     |
        |     |    
        |     O
        |   --+--
        |
        |
        |
        |
        |
        |
        |
        -----------""",
        """
        -------
        |     |
        |     |
        |     O
        |  /--+--\\
        |     |
        |     |
        |
        |
        |
        |
        |
        -----------""",
        """
        -------
        |     |
        |     |
        |     O
        |  /--+--\\
        | /   |   \\
        |     |
        |    | |
        |    | |
        |
        |
        |
        -----------""")

    #initializing variables
    goOn = "y"
    while goOn.lower() != "n":

        word = random.choice(words)
        maxWrong = len(hangman) - 1
        soFar = "_" * len(word)
        used = []

        print("Welcome to hangman. Best of luck, human")
        wrong = 0
        numTries = 0
        print(soFar)
        while wrong <  maxWrong and soFar != word:
            print(soFar)
            #print(word)
            guess = input("\n\nEnter your guess: ")
            numTries += 1
            guess = guess.lower()
            used.append(guess)
            if guess in word:
                print("\nYes! " + guess + " is in the word")
                new = ""
                print("Word length is " + str(len(word)))
                for i in range(len(word)):
                    if guess == word[i]:
                        new += guess
                    else:
                        new +=  soFar[i]
                soFar = new
                print(soFar)
                print("\nUsed: " , used)
            else:
                print("Your guess is not the word")
                print("\nUsed: " , used)
                wrong += 1

            if wrong == maxWrong:
                print(hangman[wrong])
                print("You've been hanged!")
                print("The word was " + word)
            else:
                if guess in word:
                    print("\nYou guessed it!")
                    print(soFar)
                    print("\nUsed: " , used)
                    trial = input("Would you like to guess the word? y/n: ")
                    if trial.lower() == "y":
                        answer = input("Guess is: ")
                        if answer.lower() == word:
                            print("Congratulations! You guessed the word in " + str(numTries) + " tries. You have earned 30 points")
                            break

                else:
                    print("Letter not in word")
                    print("\n" + hangman[wrong])
                    print(soFar)
                    wrong += 1
        goOn = input("Would you like to play again? y/n: ")
    input("Press any key to exit")

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

def magic8Ball():
    min = 0
    max = 4
    list = ["No way", "Go for it", "Not at this time", "What are you waiting for?", "Ask again"]
    askAgain = "yes"

    while askAgain == "yes" or askAgain == "y":
        answer = input("What issue do you seek guidance with? ")
        print("Looking into the crystal ball...")
        print("Determining outcome...")

        roll = random.randint(min, max)
        print(list[roll])

        askAgain = input("Ask again?")

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

def rockPaperScissors():
    min = 0
    max = 2
    list = ["rock", "paper", "scissors"]
    playAgain = "yes"

    while playAgain == "yes" or playAgain == "y":
        print("Let's go...")
        print("Rock, paper, scissors, and...")
        playerMove = int(input("Pick your move: rock(0), paper(1), or scissors(2) "))
        print("\nYou chose: ", list[playerMove])

        computerMove = random.randint(min, max)

        print("Computer chose: " + list[computerMove])

        if (playerMove == computerMove):
            print("It's a tie, go again" + "\n\n")
        elif (playerMove == 0 and computerMove == 1):
            print("Computer wins")
        elif (playerMove == 1 and computerMove == 0):
            print("You win")
        elif (playerMove == 0 and computerMove == 2):
            print("You win")
        elif (playerMove == 2 and computerMove == 0):
            print("Computer wins")
        elif (playerMove == 1 and computerMove == 2):
            print("Computer wins")
        elif (playerMove == 2 and computerMove == 1):
            print("You win")

        playAgain = input("Play again? ")

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
            
def diceRoll():
    count = 0
    score = 0
    highest = 0

    numPlayers = int(input("How many players? "))
    playerScores = [numPlayers]

    for x in range (numPlayers):
        count += 1
        choice = "a"
        totScore = 0
        while choice != "X":
            input("Player " + str(count) + " roll")
            score = random.randint(1,6)
            totScore = totScore + score
            print("You rolled a " + str(score) + ". You have a total of " + str(totScore))

            if totScore <= 21:
                choice = input("Would you like to roll the dice again? X to exit ")
                if (totScore > highest):
                    highest = totScore

                else:
                    continue
            else:
                print("You busted, with a score of " + str(totScore))
                choice = "X"

            choice = choice.upper()

    print("Highest score is " + str(highest))
    print("\nGoodbye")

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

def guessTheNumber():
    min = 0
    max = 100

    playAgain = "yes"

    while playAgain == "yes" or playAgain == "y":
        print("Let's go!")
        print("Thinking...")
        print("Got it!")
        guess = 0

        number = random.randint(min, max)
        while guess != number:
            guess = int(input("Pick a number between 1 and 100. "))

            if (guess == number):
                print("You guessed the number! Good job!")
            elif (guess > number):
                print("Enter a smaller number ")
            elif (guess < number):
                print("Enter a larger number ")

        playAgain = input("Play again? ")

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

def madLibs():
    answer = "y"

    while answer == "y":
        noun = input("Give me a noun: ")
        adj = input("Give me an adjective: ")
        verb = input("Give me a verb: ")
        name = input("Give me a person's name: ")
        location = input("Give me a favourite location: ")
        weapon = input("Give me a favourtie weapon: ")
        vehicle = input("Give me a vehicle: ")

        scenarios = random.randint(0,2)
        if scenarios == 1:
            print("One day, I was just stitting at the " + location + " and I noticed a(n) " + noun + " laying on the ground. The object was a(n) " + adj + " necklace.")
        elif scenarios == 0:
                print ("One day, " + name + " was walking to " + location + ", and all of a sudden you " + verb + " over with something in your hand. The object was a(n) " + adj + " necklace")
        elif  scenarios == 2:
                print("One day, one of " + name + "'s friends brought back a(n) " + adj + " rock they found while exploring."
                      "\nThey kept the rock around and soon enough, there were 5 casualties and their " + vehicle + " had stopped working."
                      "\n" + name + " and their friend had to use a " + weapon + " to destroy the " + adj + " rock, much the their friend's dismay.")
        answer = input("Do you want to go again? ")

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

def ticTacToe():
    X = "X"
    O = "O"
    empty = ""
    tie = "TIE"
    numSquares = 9
    #playAgain = "yes"

    #while playAgain == "yes" or playAgain == "y":

    def displayInstructions():
        print("""Welcome to the greatest intellectual challenge you shall face. \nIt is the showdown between you and me, your computer challenger. \nYou will make your move by identifying which number position you desire to move to.\n
            0 | 1 | 2 
            ---------
            3 | 4 | 5
            ---------
            6 | 7 | 8
            
            \nPrepare yourself. The battle begins.""")
    def askYesNo(question):
        response = None
        while response not in("y", "n"):
            response = input(question).lower()
        return response

    def askNumber(question, low, high):
        response = None
        while response not in range(low, high):
            response = int(input(question))
        return response

    def pieces():
        goFirst = askYesNo("Do you desire to go first, human? y/n: ")
        if goFirst == "y":
            print("You take the first move. You will need it.")
            human = X
            computer = O
        else:
            print("Your bravery will be your undoing... I will go first")
            computer = X
            human = O
        return computer, human

    def newBoard():
        board = []
        for square in range(numSquares):
            board.append(empty)
        return board

    def displayBoard(board):
        print("\n " + board[0] + " | " + board[1] + " | " + board[2])
        print("----------")
        print("\n " + board[3] + " | " + board[4] + " | " + board[5])
        print("----------")
        print("\n " + board[6] + " | " + board[7] + " | " + board[8])

    def legalMoves(board):
        moves = []
        for square in range(numSquares):
            if board[square] == empty:
                moves.append(square)
        return moves

    def winner(board):
        waysToWin = ((0,1,2), (3,4,5), (6,7,8), (0,3,6), (1,4,7), (2,5,8), (0,4,8), (2,4,6))
        for row in waysToWin:
            if board[row[0]] == board[row[1]] == board[row[2]] != empty:
                winner = board[row[0]]
                return winner
        if empty not in board:
            return tie
        else:
            return None

    def humanMove(board, human):
        legal = legalMoves(board)
        move = None
        while move not in legal:
            move = askNumber("\nWhere will put your piece, human? (0-8): " , 0 , numSquares)
            if move not in legal:
                print("\nThat square is already occupied. Foolish. Choose another.")
        print("Fine...")
        return move

    def computerMove(board, computer, human):
        board = board[:]
        bestMoves = (4, 0, 2, 6, 8, 1, 3, 5, 7)
        print("\nI shall take square number " , end = "")

        #if computer can win, take square

        for move in legalMoves(board):
            board[move] = computer
            if winner(board) == computer:
                print(move)
                return move
            board[move] = empty

        #if human can win, block move

        for move in legalMoves(board):
            board[move] = human
            if winner(board) == human:
                print(move)
                return move
            board[move] = empty

        #tie

        for moves in bestMoves:
            if move in legalMoves(board):
                print(move)
                return move

    def nextTurn(turn):
        if turn == X:
            return O
        else:
            return X

    def congratWinner(theWinner, computer, human):
        if theWinner != tie:
            print("\n" + theWinner + " won!\n")
        else:
            print("\nIt's a tie.\n")

        if theWinner == computer:
            print("As predicted, I am triumphant once more.\n")
            #playAgain = input("Play again? ")
        elif theWinner == human:
            print("No! No! You tricked me, human!")
            #playAgain = input("Play again? ")
        elif theWinner == tie:
            print("You are most lucky, human. You managed a draw.")
            #playAgain = input("Play again? ")

    #--------------------------------------------------------------------------------

    def main():
        displayInstructions()
        computer, human = pieces()
        turn = X
        board =  newBoard()
        displayBoard(board)

        while not winner(board):

            if turn == human:
                move = humanMove(board, human)
                board[move] = human
            else:
                move = computerMove(board, computer, human)
                board[move] = computer
            displayBoard(board)
            turn = nextTurn(turn)
        theWinner = winner(board)
        congratWinner(theWinner, computer, human)

    #start program

    main()

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

def critterCaretaker():
    class Critter(object):
        '''a virtual pet'''
        def __init__(self, name, hunger = "", fun = ""):
            print("A new critter called " + name + " has been created!")
            self.name = name
            self.hunger = random.randrange(0,20)
            self.fun = random.randrange(0,20)

        def __str__(self):
            '''to see hunger and fun levels'''
            return self.name, self.hunger, self.fun

        def health(self):
            '''check the health of a critter'''
            health = self.fun + self.hunger
            if health < 5:
                print(self.name + " is very happy and healthy!")
            if 5 <= health <= 15:
                print(self.name + " is doing good!")
            if 16 <= health <= 25:
                print(self.name + " is okay right now!")
            if 26 <= health <= 35:
                print(self.name + " needs some attention. Maybe try feeding or playing with them!")

        def talking_one(self):
            '''what the critter will say when spoken to'''
            self.__pass_time()
            what_to_say = random.randrange(0,5)
            if what_to_say == 0:
                print("I like the colour red.")
            elif what_to_say == 1:
                print("I am very sleepy today.")
            elif what_to_say == 2:
                print("Today is today. I think...")
            elif what_to_say == 3:
                print("I ate my shoe.")
            elif what_to_say == 4:
                print("Give me your money!")
            else:
                print("I don't want to talk anymore. Leave me alone.")

        def talking_all(self):
            '''when talking to all critters'''
            self.__pass_time()

        def feeding_one(self):
            '''feeding one critter'''
            self.__pass_time()
            self.hunger -= 4
            if self.hunger < 0:
                self.hunger = 0
            print(self.name + " says: Yummy! That was a nice snack! Thanks!")

        def feeding_all(self):
            '''feeding all the critters'''
            self.__pass_time()
            self.hunger -= 4
            if self.hunger < 0:
                self.hunger = 0

        def play_one(self):
            '''play with one critter'''
            self.__pass_time()
            self.fun -= 4
            if self.fun < 0:
                self.fun = 0
            if self.fun > 20:
                self.fun = 20
            print(self.name + " says: That was great fun! Thanks for playing with me!")

        def play_all(self):
            """play with all thr critters"""
            self.__pass_time()
            self.fun -= 4
            if self.fun < 0:
                self.fun = 0
            if self.fun > 20:
                self.fun == 20

        def __pass_time(self):
            '''simulates passing of time'''
            self.hunger += 1
            self.fun += 1
            if self.hunger > 20:
                self.hunger ==20
            if self.fun > 20:
                self.fun == 20

    #creating critters, and storing them in the critlist list

    dave = Critter('DAVE')
    sarah = Critter('SARAH')
    clair = Critter('CLAIR')
    ashie = Critter('ASHIE')
    daen = Critter('DAEN')
    critlist = []
    critlist.append(dave.__str__())
    critlist.append(sarah.__str__())
    critlist.append(clair.__str__())
    critlist.append(ashie.__str__())
    critlist.append(daen.__str__())

    def main():
        print("""
        \t\tWelcome to your critter farm!
        \t\tSelect one of the options below to interact with them!

        0 - exit
        1 - play with one critter
        2 - play with all the critters
        3 - feed one critter
        4 - feed all the critters
        5 - talk with a critter
        6 - talk to all the critters
        7 - view the health of a critter
        """)

        answer = ""
        while answer != '0':
            answer = input("\nSelect your option: ")
        #exit the program
            if answer == '0':
                print("Logging out... Goodbye!")
        #play with a critter
            if answer == '1':
                who2 = input("Enter the name of the critter you want to play with. \nDave, Sarah, Clair, Ashie, or Daen?: ")
                who = who2.upper()
                if who == 'DAVE':
                    dave.play_one()
                    print("That was fun!")
                elif who == 'SARAH':
                    sarah.play_one()
                    print("Sarah says 'Let's play again!'")
                elif who == 'CLAIR':
                    clair.play_one()
                    print("Clair says 'Wee! Again, again!")
                elif who == 'ASHIE':
                    ashie.play_one()
                    print("Ashie says 'I'm happy now!'")
                elif who == 'DAEN':
                    daen.play_one()
                    print("Daen says 'Is that all you've got?'")
                else:
                    print("That critter does not exist. Try again.")
                    who2 = input("Enter the name of the critter you want to play with \nDave, Sarah, Clair, Ashie, or Daen?: ")
                    who = who2.upper()
                    
        #play with all critters
            if answer == '2':
                dave.play_all()
                sarah.play_all()
                clair.play_all()
                ashie.play_all()
                daen.play_all()
                print("All the critters say 'Hurray for our wonderful owner playing with us!\nSuch a fun group game with all of us!'")

        #feeding a critter
            if answer == '3':
                who = input("Enter the name of the critter you want to feed. \nDave, Sarah, Clair, Ashie, or Daen?: ")
                who = who.upper()
                print("Who is " + who)
                if who == "DAVE":
                    dave.feeding_one()
                elif who == "SARAH":
                    sarah.feeding_one()
                elif who == "CLAIR":
                    clair.feeding_one()
                elif who == "ASHIE":
                    ashie.feeding_one()
                elif who == "DAEN":
                    daen.feeding_one()
                else:
                    print("That critter does not exist. Try again.")
                    who = input("Enter the name of the critter you want to feed. \nDave, Sarah, Clair, Ashie, or Daen?: ")
                    who = who.upper()

        #feeding all the critters
            if answer == '4':
                dave.feeding_all()
                sarah.feeding_all()
                clair.feeding_all()
                ashie.feeding_all()
                daen.feeding_all()
                print("Thank you! We're all so grateful!")

        #talking with a critter
            if answer == '5':
                who = who = input("Who do you want to talk with? \nDave, Sarah, Clair, Ashie, or Daen?: ")
                who = who.upper()
                if who == 'DAVE':
                    dave.talking_one()
                elif who == 'SARAH':
                    sarah.talking_one()
                elif who == 'CLAIR':
                    clair.talking_one()
                elif who == 'ASHIE':
                    ashie.talking_one()
                elif who == 'DAEN':
                    daen.talking_one()

        #talking with all the critters
            if answer == '6':
                dave.talking_all()
                sarah.talking_all()
                clair.talking_all()
                ashie.talking_all()
                daen.talking_all()
                what_they_say = random.randrange(0,5)
                if what_they_say == 0:
                    print("We are an angry mob!")
                if what_they_say == 1:
                    print("Three cheers for our owner!")
                if what_they_say == 2:
                    print("We are a happy mob!")
                if what_they_say == 3:
                   print("We all agree with you.")
                if what_they_say == 4:
                    print("Yes master, we will do as you command.")
                if what_they_say == 5:
                    print("Begin Operation: World Domination!")

        #View a critter's health
            if answer == '7':
                who2 = input("Enter the name of the critter you want check on. \nDave, Sarah, Clair, Ashie, or Daen?: ")
                who = who2.upper()
                if who == 'DAVE':
                    dave.health()
                elif who == 'SARAH':
                    sarah.health()
                elif who == 'CLAIR':
                    clair.health()
                elif who == 'ASHIE':
                    ashie.health()
                elif who == 'DAEN':
                    daen.health()

        #hidden from user, will show the list that they're all contained in
        #view their hunger + fun levels
            if answer == 'moreinfo':
                updatelist = []
                updatelist.append(dave.__str__())
                updatelist.append(sarah.__str__())
                updatelist.append(clair.__str__())
                updatelist.append(ashie.__str__())
                updatelist.append(daen.__str__())
                
    main()

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

def wordle():
    class wordle:
        global hidden_word

        def game_instruction(self):
            print("""Wordle is a single player game.\n
                    A player has to guess a five letter hidden word.\n
                    \ta) You have six attempts.\n
                    \tb) Your progress Guide \u2713 \u03C7 \u2629
                    \n\t\t1. \u2713 indicates that the letter at that position was guessed correctly.
                    \n\t\t2. \u2629 indicated that the letter at that position is in the word at a different position.
                    \n\t\t3. \u03C7 indicates that the letter at that position is wrong and isn't in the word.\n""")
            #\u03C7 is the X
            #\u2713 is the check
            #\u2629 is the +

        def check_word(self):
            attempt = 6
            while attempt > 0:
                guess = str(input("Guess the word: "))
                if guess == hidden_word:
                    print("Your guessed the word correctly!")
                    break
                else:
                    attempt = attempt - 1
                    print(f"You have " + str(attempt) + " attempt(s) left\n")
                    for char, word in zip(hidden_word, guess):
                        if word in hidden_word and word in char:
                            print(word + "\u2713")
                        elif word in hidden_word:
                            print(word + "\u2629")
                        else:
                            print(word + "\u03C7")
                if attempt == 0:
                    print(f"Game over! \nThe word was " + hidden_word)

        def pickWord(self):
            WORDS = ("light", "slide", "paper", "phone", "build", "watch", "spray", "fight", "glide", "truck", "spoil", "gloss", "write", "right", "store", "tries", "check", "wrong", "guess", "final", "first", "third", "props", "input", "while", "puppy", "sleep", "grand", "grade", "class", "glass", "flows", "river", "stand", "house", "mouse", "louse", "stows", "blows", "heave", "leave", "eaves", "caves", "straw", "video", "yahoo", "marry", "weave", "reset", "scold", "water", "jazzy", "dizzy", "quack", "books", "queen", "phlox", "bikes", "nymph", "chalk", "shark", "cheek", "purge", "flock", "quill", "quilt", "stars", "quite", "quiet", "quote", "queue", "razor", "rock", "remix", "smoky", "tacky", "witty", "wryly")
            global hidden_word
            hidden_word = random.choice(WORDS)
            #print(f"\nword is  {hidden_word}")

    def mainline():
        words = wordle()
        words.game_instruction()
        goOn = "y"
        while goOn.lower() != "n":
            words.pickWord()
            words.check_word()
            goOn = input("Would you like to play again? y/n ").lower()
        print("\n\nThanks for playing!")


    mainline()

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

def gameChoice():
    game = int(input("What would you like to play? "))
    print("\n")
    if game == 1:
        hangman()
    elif game == 2:
        rockPaperScissors()
    elif game == 3:
        magic8Ball()
    elif game == 4:
        guessTheNumber()
    elif game == 5:
        madLibs()
    elif game == 6:
        ticTacToe()
    elif game == 7:
        critterCaretaker()
    elif game == 8:
        wordle()
    elif game == 9:
        diceRoll()
    else:
        coinToss()

def startMsg():
    print("\nWelcome to the Game Room! \nWhen asked a yes or no question, please answer with y or n \nHere are the games you can play:\n")
    print("Hangman(1)\nRock Paper Scissors(2)\nMagic 8 Ball(3)\nGuess the Number(4)\nMad Libs(5)\nTic Tac Toe(6)\nCritter Caretaker(7)\nWordle(8)\n21(9)\nCoin Toss(10)\n")

#----------------------------------------------------------------------------------------------------------------

while play == "y":
    startMsg()
    gameChoice()
