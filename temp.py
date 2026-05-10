'''grade = float(input("Enter grade earned: "))
letter = ""
if (grade > 89.5):
    letter = "A"
elif (grade > 79.5):
    letter = "B"
elif (grade > 69.5):
    letter = "C"
elif (grade > 59.5):
    letter = "D"
else:
    letter = "F"

print ("Your grade of " + str(grade) + " is a(n) " + letter)'''

#======================================================================================================

'''payRate = float(input("Enter Pay Rate: "))
hours = int(input("Enter hours worked (whole numbers only): "))
grossPay = 0
if (hours > 40):
    grossPay = (hours - 40) * payRate * 1.5 + 40 * payRate
else:
    grossPay = hours * payRate

print(str(payRate) + " for " + str(hours)
      + " hours results in a gross pay of " + str(grossPay))'''

#=======================================================================================================

'''highScore = 95
test1 = int(input("Enter test1 grade: "))
test2 = int(input("Enter test2 grade: "))
test3 = int(input("Enter test3 grade: "))

#Calculate average
average = (test1 + test2 + test3)/3.0
print("Your average is: " + str(average))
if average > highScore:
    print ("Great job! Keep it up!")
else:
    print ("Keep trying!")'''

#=======================================================================================================

'''import random

print(random.randint(1,20))'''

#=======================================================================================================

'''i = 1
while i < 6:
    print(i)
    i += 1'''

#=======================================================================================================

#Magic 8-Ball

'''import random
min = 0
max = 4
list = ["No way", "Go for it", "Not at this time", "What are you waiting for?", "Ask again"]
rollAgain = "yes"

while rollAgain == "yes" or rollAgain == "y":
    answer = input("What issue do you seek guidance with? ")
    print("Looking into the crystal ball...")
    print("Determining outcome...")

    roll = random.randint(min, max)
    print(list[roll])

    rollAgain = input("Roll the dice again?")'''

#========================================================================================================

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

#Mad Libs

'''import random
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
            print("One day, one of " + name + "s friends brought back a(n) " + adj + " rock they found while exploring."
                  "\nThey kept the rock around and soon enough, there were 5 casualties and their " + vehicle + " had stopped working."
                  "\n" + name + " and their friend had to use a " + weapon + " to destroy the " + adj + " rock, much the their friend's dismay.")
    answer = input("Do you want to go again? ")'''

#============================================================================================================

#Dice Roll

'''import random

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
            choice = input("Would you like to roll the dice again? X to exit")
            if (totScore > highest):
                highest = totScore

            else:
                continue
        else:
            print("You busted, with a score of " + str(totScore))
            choice = "X"

        choice = choice.upper()

print("Highest score is " + str(highest))
print("\nGoodbye")'''

#===========================================================================================================

#Rock Paper Scissors

'''import random
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

    playAgain = input("Play again? ")'''

#=============================================================================================================

#Guess the Number

'''import random
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

    playAgain = input("Play again? ")'''
            
#==========================================================================================================
#Hangman

import random
points = 0

dict = {"name": "Katherine","Title": "student"}
for each in dict:
    print(dict)
#constants
words = ("overused", "clam", "guam", "end of semester", "prom", "homework")

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
        print(word)
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
            else:
                print("Letter not in word")
                print("\n" + hangman[wrong])
                print(soFar)
                trial = input("Would you like to guess the word? y/n: ")
                if trial.lower() == "y":
                    answer = input("Guess is: ")
                    if answer.lower() == word:
                        print("Congratulations! You guessed the word in " + str(numTries) + " tries. You have earned 30 points")

                    else:
                        wrong += 1
    goOn = input("Would you like to play again? y/n: ")
input("Press any key to exit")

#=====================================================================================================

#card game with computer

'''import random

compPlayer = random.randint(0,51)
Player = random.randint(0,51)

print("Computer's card is " + str(compPlayer))
print("Your card is " + str(Player))

if (compPlayer > Player):
    print("Computer goes first")
else:
    print("You go first")'''

#=====================================================================================================

'''#odd numbers

i = 0

while (i < 21):
    ans = (i%2)
    if (ans != 0):
        
        print(str(i) + " is odd number" )
    i += 1
print("\n")
#even numbers

for i in range (0,21):
    ans = (i%2)
    if (ans != 1):
        
        print(str(i) + " is even number" )
    i += 1'''

#=====================================================================================================

'''more = "y"
while more == "y" or more == "yes":
    grade = float(input("Enter grade earned: "))
    letter = ""
    if (grade > 89.5):
        letter = "A"
    elif (grade > 79.5):
        letter = "B"
    elif (grade > 69.5):
        letter = "C"
    elif (grade > 59.5):
        letter = "D"
    else:
        letter = "F"

    print ("Your grade of " + str(grade) + " is a(n) " + letter)
    more = input("More to grade? ")'''

#=====================================================================================================

'''#password generator

import random
password = ""

listOfCharacters = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z", "a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z", "0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "$", "#", "@"]

for i in range (0,13):
    password += random.choice(listOfCharacters)
print("\nYour password is " + password + "\n")'''
   
