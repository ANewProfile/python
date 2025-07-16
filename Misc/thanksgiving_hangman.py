import random

#intro
intro2 = True
while intro2 == True:
    intro = input(
    "Welcome to thanksgiving hangman, you have 7 wrong guesses to guess the thanksgiving word. Would you like to play([y]es or [n]o)? ")
    if intro.lower() == "y":
        print("Awesome! Game on.")
        intro2 = False
    elif intro.lower() == "n":
        print("Okay. Be sure to play another time!")
        intro2 = False
        break
    else:
        print("Invalid, type either y or n")

# words and board
words = ["thanksgiving", "turkey", "stuffing", "gravy", "mayflower", "fall"]
word = random.choice(words)
board = len(word)*["-"]
tries = 0

# game loop
while True:
    if intro == "n":
        break
    else:
        wrong = True
        guess = input("Guess a letter ")
        for i,letter in enumerate(word):
            if guess == letter:
                board[i] = letter
                wrong = False
        print("".join(board))
        if wrong == True:
            tries += 1
        if tries == 7:
            print("Sorry you lose.")
            print("The word was " + str(word) + ".")
            break
        if "-" not in board:
            print("Correct!")
            break