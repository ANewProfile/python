#import packages
import re
import requests
import random
import termcolor

# get list of words, choose a word, and find letters
meaningpedia_resp = requests.get(
    "https://meaningpedia.com/5-letter-words?show=all")
pattern = re.compile(r'<span itemprop="name">(\w+)</span>')
word_list = pattern.findall(meaningpedia_resp.text)
random.shuffle(word_list)
word = word_list[0]

# intro
print("Welcome to Wordle Extreme! Get ready, because this is going to be difficult.")

# game loop and variables
guesses = 0
go = True
current_index = 0
correct_indices = set()

while go and guesses < 6:
    guess = input("Please enter a five letter word: ")
    if guess not in word_list:
        print(termcolor.colored(
            f"not a 5-letter word my primitive brain understands, please guess again", "red", attrs=["bold"]))
        continue

    guesses += 1
    if guess == word:
        print(termcolor.colored(f"{word}", "blue", attrs=["bold"]))
        print(f"You guessed the word in {guesses} tries!")
        break

    guessed_letter_in_word_counter = [word.count(letter) for letter in guess]
    correctly_guessed_letters = [letter if word[i] ==
                                 letter else None for i, letter in enumerate(guess)]

    for i, letter in enumerate(guess):
        if letter == word[i]:
            print(termcolor.colored(f"| {letter} |", "green", attrs=["bold"]))
        elif letter in word:
            number_of_times_letter_can_be_in_wrong_pos = guessed_letter_in_word_counter[i]-correctly_guessed_letters.count(
                letter)
            if number_of_times_letter_can_be_in_wrong_pos <= 0:
                print(f"| {letter} |")
            else:
                print(termcolor.colored(
                    f"| {letter} |", "magenta", attrs=["bold"]))
                guessed_letter_in_word_counter[i] -= 1
        else:
            print(f"| {letter} |")

if guesses == 6:
    print(termcolor.colored(
        f"You lose! The word was {word}", "red", attrs=["bold"]))
