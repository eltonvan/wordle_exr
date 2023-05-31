# wordle game
import random
import re
from pathlib import Path
# set path to wordlist
local_file_path = Path.cwd() / 'wordlist.txt'
last_guess=''

def random_word():
    '''generate random word from textfile'''
    # open file
    file_path = Path.cwd() / 'wordlist.txt'
    # read file and split into list of words
    file=open(file_path, 'r')
    text = file.read()
    words = text.split()
    # generate random number and return word at index
    i = random.randint(0, len(words)-1)
    return words[i]

def check_guess(word, guess):
    global last_guess
    '''check if guess is correct'''
    # check if guess is same length as word
    if len(guess) != len(word):
        return False
    print(last_guess)
    current_guess=''
    # check if guess is in word
    for i in range(len(word)):
        if guess[i] == word[i]:
            #print(guess[i], end="")
            current_guess += guess[i]
        elif guess[i] in word:
            #print("-", end="")
            current_guess += "-"
        else:
            #print("X", end="")
            current_guess += "X"
    print(current_guess)
    last_guess += "\n" + current_guess + " " + guess
    return guess == word

def wordle():
    '''game'''
    word = random_word()
    
    print("Guess a five-letter word.")
    print(" '-' is correct letter, wrong position.")
    print("'X' is wrong letter.")
    print("You have 6 attempts.")
    print("-------------------------------")
    # loop until 6 attempts
    attempts = 0
    while attempts < 6:
        # get guess from user
        guess = input("Enter a five letter word: ").lower()
        # check if guess is valid
        if len(guess) != 5:
            print("wrong! Please enter a five-letter word.")
            continue
        # check if guess is correct
        if check_guess(word, guess):
            print(" Congratulations!!! You won")
            break
        attempts += 1
        print(f"  Attempts remaining: {6 - attempts}")
        print("-------------------------------")
    else:
        print(f"Game over! The word was {word}.")
    
    print()

    
wordle()




