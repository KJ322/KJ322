#username
'''
username = input("Choose a username (4-10 characters): ")

if 4 < len(username) <=10:
    print(f"Thank you, the username " + username + " is valid")
else:
    print("The username must be between 4 and 10 characters")'''

#===================================================================

'''list1 = ['physics', 'chemistry', 1997, 2000];
list2 = [ 1, 2, 3, 4, 5, 6, 7];

print("list1[0]: " + list1[0])
print("list2[1:5]: " + str(list2[1:5]))'''

#===================================================================

'''list = ['physics', 'chemistry', 1997, 2000];

print("Value available at index 2: ")
print(list[2])
list[2] = 2001;
print("New value available at index 2: ")
print(list[2])'''

#===================================================================

'''list = ['physics', 'chemistry', 1997, 2000];

print(list)
del list[2];
print("After deleting value at index 2: ")
print(list)'''

#===================================================================

'''usernames = []

print("Enter three options for your username")

while len(usernames) < 3:
    username = input("Choose a username (4-10 characters): ")
    if 4 < len(username) <= 10:
        print(f"Thank you, the username " + username + " is valid")
        usernames.append(username)
    else:
        print("The username must be between 4 and to characters")

print(usernames)'''

#===================================================================

'''def square(number):
    result = number ** 2
    return result

num = int(input("Enter a number to square: "))
print(str(square(num)) + " is " + str(num) + " squared")'''

#===================================================================

'''className = "SGD 113"
def displayHello():
    name = input("Enter your name: ")
    print("Hello, " + name + ", welcome to functions")
    variablePassedExample(newName)
    ready = ask_yes_no("Are you ready? ")
    if ready == "y":
        print("Let's go!")

def variablePassedExample(newName):
    print("Welcome to " + className + ", " + newName)

def ask_yes_no(Question):
    response = None
    while response not in ("y", "n"):
        response = input(Question).lower()
        return response

displayHello()'''

#===================================================================

'''def getName():
    name = input("Please type in your name: ")
    return name

def printme(str):
    print(str)
    return

def changeme(mylist):
    mylist.append((1, 2, 3, 4));
    print("Values inside the function: " + str(mylist))
    return

def changeme(mylist):
    mylist = [10, 20, 30];
    print("Values outside the function: " + str(mylist))
    return

def getAge():
    age = int(input("Please enter your age: "))
    return age

def getInfo():
    name = getName()
    age = getAge()
    printinfo(name, age)
    return

def printinfo(name, age):
    print("Name: " + name)
    print("Age: " + str(age))
    return;

def sum(arg1, arg2):
    total = arg1 + arg2
    print("inside the function: " + str(total))
    return total;

def main():
    print(getName())
    mylist = ["first", "second", "third", "fourth"]
    printme("This is string passed into printme")
    changeme(mylist)
    print("MyList outside of function: " + str(mylist))
    getInfo()
    sum(10, 20)
    return

main()'''

#================================================================

'''import random

words = ("python", "jumble", "easy", "difficult", "answer", "xylophone", "dexter", "necessary", "snake", "exception", "koala", "coding", "wednesday", "february", "monty", "pluto", "jupiter", "tardis", "quartz", "sphinx", "bologna", "ticondiroga", "opportunity", "curiosity", "mars")
goOn = "y";
correct = ""
jumble = ""
attempts = 0
maxAttempts = 2

def guessTheJumble():
    attempts = 0
    print("\nThe jumble is " + jumble)
    #print("Word is: " + correct)
    guess = input("\nYour guess: ")
    while guess != correct and guess != "":
        print("Sorry, that's not it")
        attempts += 1
        guess = input("Your guess: ")
        if attempts == maxAttempts:
            print("Sorry! You couldn't guess it. The word was " + correct)
            print("That's it! Thanks for playing!")
             
    print("That's it! Thanks for playing!")

def startMsg():
    print("******* Welcome to Jumble Word! *******")
    print("\nUnscramble the word to win")

def jumbleWord():
    word = random.choice(words)
    correct = word
    while word in words:
        jumble = ""
        while word:
            position = random.randrange(len(word))
            jumble += word[position]
            word = word[:position] + word[position+1:]
    return jumble, correct

#Processing

startMsg()
while (goOn == "y"):
    jumble, correct = jumbleWord()
    guessTheJumble()
    goOn = input("Want to play again? y/n? ");
print("\n\nPress enter to exit")'''

#=====================================================================

#21

'''import random
global count, score, highest

def initialization():
    global score
    score = 0
    global highest
    highest = 0

    global numPlayers
    numPlayers = int(input("How many players? "))
    global playerScores
    playerScores = [numPlayers]

def playGame():
    global numPlayers
    count = 0
    for x in range(numPlayers):
        global highest
        count += 1
        choice = "a"
        totScore = 0
        while (choice.upper() != "X"):
            input("Player " + str(x+1) + " roll")
            score = random.randint(1,6)
            totScore = totScore + score
            print("You rolled a " + str(score) + ". You have a total of " + str(totScore))

            if numPlayers > 1:
                if totScore <= 21:
                    choice = input("Would you like to roll again? X to exit ")
                    if (totScore > highest):
                        highest = totScore
                        num = count
                    else:
                        continue
                else:
                    print("You busted, with a score of " + str(totScore))
                    choice = "X"
                    choice = choice.upper()
                print(f"\nPlayer number " + str(num) + " has won")

            else:
                if totScore <= 21:
                    choice = input("Would you like to roll again? X to exit ")
                    if (totScore > highest):
                        highest = totScore
                        num = count
                        print("Your highest is " + str(highest))
                else:
                    print("You busted, with a score of " + str(totScore))
                    

               
#-------------------------------------------------------------------------

def mainline():
    goOn = "y"
    while goOn.lower() == "y":
        initialization()
        playGame()
        goOn = input("Would you like to play again? y/n? ")

    print("Highest score is " + str(highest))
    print("\nGoodbye")

mainline()'''

#========================================================================

#Tic Tac Toe

'''import random

X = "X"
O = "O"
empty = ""
tie = "TIE"
numSquares = 9

def displayInstructions():
    print("""Welcome to the greatest intellectual challenge you shall face. \nIt is the show down between you and me, your computer challenger. \nYou will make your move by identifying which number position you disire to move to.\n
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
            print("\nThat square is already occupied. Foolish. Choose another (y/n): ")
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
        print(theWinner + " won!\n")
    else:
        print("\nIt's a tie.\n")

    if theWinner == computer:
        print("As predicted, I am triumphant once more.\n")
    elif theWinner == human:
        print("No! No! You tricked me, human!")
    elif theWinner == tie:
        print("You are most lucky, human. You managed a draw.")

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

main()'''

#===============================================================================

'''import random

class Critter(object):
    ''a virtual pet''
    def __init__(self, name, hunger = "", fun = ""):
        print("A new critter called " + name + " has been created!")
        self.name = name
        self.hunger = random.randrange(0,20)
        self.fun = random.randrange(0,20)

    def __str__(self):
        ''to see hunger and fun levels''
        return self.name, self.hunger, self.fun

    def health(self):
        ''check the health of a critter''
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
        ''what the critter will say when spoken to''
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
        ''when talking to all critters''
        self.__pass_time()

    def feeding_one(self):
        ''feeding one critter''
        self.__pass_time()
        self.hunger -= 4
        if self.hunger < 0:
            self.hunger = 0
        print(self.name + " says: Yummy! That was a nice snack! Thanks!")

    def feeding_all(self):
        ''feeding all the critters''
        self.__pass_time()
        self.hunger -= 4
        if self.hunger < 0:
            self.hunger = 0

    def play_one(self):
        ''play with one critter''
        self.__pass_time()
        self.fun -= 4
        if self.fun < 0:
            self.fun = 0
        if self.fun > 20:
            self.fun = 20
        print(self.name + " says: That was great fun! Thanks for playing with me!")

    def play_all(self):
        ""play with all thr critters""
        self.__pass_time()
        self.fun -= 4
        if self.fun < 0:
            self.fun = 0
        if self.fun > 20:
            self.fun == 20

    def __pass_time(self):
        ''simulates passing of time''
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
                
main()'''

#=========================================================================================================

from tkinter import Tk, Label, Button
import time
import random

class myFirstGUI:
    
    def __init__(self, master):
        random.seed()
        self.turn_number = 1
        self.playing_round = False

        self.master = master
        master.title("Simon Says")

        self.label = Label(master, text="Let's Play Simon Says!")
        self.label.grid(row=0, column=0, columnspan=2)

        #creat and place buttons in GUI

        self.red_button = Button(master, text="Red", bg='white', command=self.red)
        self.red_button.grid(row=1, column=0)

        self.green_button = Button(master, text="Green", bg='white', command=self.green)
        self.green_button.grid(row=1, column=1)

        self.blue_button = Button(master, text="Blue", bg='white', command=self.blue)
        self.blue_button.grid(row=2, column=0)

        self.yellow_button = Button(master, text="Yellow", bg='white', command=self.yellow)
        self.yellow_button.grid(row=2, column=1)

        self.play_button = Button(master, text="Play!", command=self.play)
        self.play_button.grid(row=3, column=0, columnspan=2)

        self.close_button = Button(master, text="Close", command=master.quit)
        self.close_button.grid(row=4, column=0, columnspan=2)

    def press_color_button(self, button_color):
        self.flash_button(button_color)
        if self.playing_round == True:
            if self.button_sequence and self.button_sequence[0] == button_color:
                print("Correct!")
                self.button_sequence.pop(0)
            else:
                print("Oops! The correct button was %s!" % self.button_sequence[0])
                print("You lose!")
                self.playing_round = False
                self.turn_number = 1
        else:
            print(button_color + "!")

    def red(self):
        self.press_color_button("red")

    def green(self):
        self.press_color_button("green")

    def blue(self):
        self.press_color_button("blue")

    def yellow(self):
        self.press_color_button("yellow")

    def poll_user_input(self):
        if len(self.button_sequence) > 0:
            self.master.after(100, self.poll_user_input) #runs every 100 milliseconds
        else:
            print("You win!")
            self.turn_number += 1

    def reset_to_white(self, which_button):
        which_button.configure(bg='white')

    def flash_button(self, which_button):
        print("HERE I AM and button is " + which_button)
        if which_button == "red":
            self.red_button.configure(bg="red")
            self.master.after(500, self.reset_to_white, self.red_button)

        if which_button == "blue":
            self.blue_button.configure(bg="blue")
            self.master.after(500, self.reset_to_white, self.blue_button)

        if which_button == "green":
            self.green_button.configure(bg="green")
            self.master.after(500, self.reset_to_white, self.green_button)

        if which_button == "yellow":
            self.yellow_button.configure(bg="yellow")
            self.master.after(500, self.reset_to_white, self.yellow_button)

    def play(self):
        self.playing_round = True
        print("Let's play! Remember the color patterns, then press them in order!")
        print("Ready... remember this!")
        
       
        #
        for num in range(self.turn_number):
            which_button = random.choice(["red", "yellow", "blue", "green"])
            self.button_sequence.append(which_button)
            self.flash_button(which_button)
            
            self.master.after((num*1100), self.flash_button, which_button)

        print("Now it's your turn! Press the buttons in the right order!")
        self.poll_user_input()

root = Tk()

my_gui = myFirstGUI(root)

root.mainloop()

#================================================================================================================

'''import random
class wordle:
    global hidden_word

    def game_instruction(self):
        print("""Wordle is a single player game.\n
                A player has to guess a five letter hidden word.\n
                \ta) You have six attempts.\n
                \tb) Your progress Guide \u2713 \u03C7 \u03C7 \u2713 \u2629
                \n\t\t1. \u2713 indicates that the letteraat that position was guessed correctly.
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


mainline()'''
