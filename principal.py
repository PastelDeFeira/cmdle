import json
import random
import re

def game_loop():
    # load all 4 letter words
    with open('4_letter_words.json', 'r') as file:
        words_data = json.load(file)

    # load words list as list
    words_list = [entry['word'].lower() for entry in words_data]

    # choose a random word from the list
    random_word = random.choice(words_list)
    print(random_word)

    # split random word into individual characters
    word_chars = list(str(random_word))
    print(word_chars)

    user_guess = input("Guess a 4 letter word: ")
    user_chars = list(user_guess.lower())

    # limits user's guess to 4 chars only
    if len(user_guess) != 4:
        print("Use only letters for your guess!")

    # makes sure user's guess is a valid word
    if user_guess not in words_list:
        print("Enter a valid word!")
        print("a")

    print(user_chars)

while True:
    game_loop()