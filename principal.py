import json
import random
import os

# load all 4 letter words
with open('4_letter_words.json', 'r') as file:
    words_data = json.load(file)

# load words list as list
words_list = [entry['word'].lower() for entry in words_data]

# choose a random word from the list
random_word = random.choice(words_list)

# split random word into individual characters
word_chars = list(str(random_word))

# clears terminal
os.system('cls')

print("Welcome to Wordle But Bad!")
playing = input("Play now? y/n ")

if playing == "y":
    playing = True

elif playing == "n":
    quit()

def guess():
    guesses = 1

    # limits to 6 guesses
    while guesses < 6:
        user_guess = input('Guess a 4 letter word (Guess %s/5): ' % guesses)
        
        # splits user's guess into individual characters
        user_chars = list(user_guess.lower())
        correct_chars = 0

        # limits user's guess to 4 chars only
        if len(user_guess) != 4:
            print("Your guess should be only 4 letters long...")
            break

        # makes sure user's guess is a valid word
        if user_guess not in words_list:
            print("Enter a valid word!")
            break

        # if user guesses correctly prompt to play again
        if user_guess == random_word:
            print(f'Congratulations, you guessed "{random_word}" correctly!')
            print(f'You guessed in {guesses} guesses!')
            play_again()
            playing == False


        # check's if there are any characters which the user guessed that are also in the correct word
        # also checks if the user inputted any characters already in the correct position
        for i, (user_char, word_char) in enumerate(zip(user_chars, word_chars)):
            if user_char == word_char:
                print(f'The letter {user_char} is at the correct position!')

            elif user_char in word_chars:
                print(f'The letter {user_char} is correct, but not in the correct position!')

        # prints how many characters are correct
        if correct_chars > 0:
            print("%s/4 characters correct" % correct_chars)

        guesses = guesses + 1
       
       # if user goes over guess limit prompt to play again
        if guesses == 6:
            print(f'You were not able to guess the word, the word was "{random_word}"...')
            play_again()
            playing == False
        
# self explanatory
def play_again():
    play_again = input("Play again? y/n ")
    if play_again == "y":
        playing == True
    
    else:
        quit()

# runs gameloop after player wants to play
while playing == True:
    guess()