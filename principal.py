import json
import random

playing = True

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

def guess():
    guesses = 1
    while guesses < 6:
        user_guess = input('Guess a 4 letter word (Guess %s/5): ' % guesses)
        
        # splits user's guess into individual characters
        user_chars = list(user_guess.lower())
        correct_chars = 0

        # limits user's guess to 4 chars only
        if len(user_guess) != 4:
            print("Use only letters for your guess!")
            break

        # makes sure user's guess is a valid word
        if user_guess not in words_list:
            print("Enter a valid word!")
            break

         # if user guesses correctly prompt to play again
        if user_guess == random_word:
            print("Congratulations, you guessed %s correctly!" % random_word)
            print(f'You guessed in {guesses} guesses!')
            play_again()
            playing == False


        # check's if there are any characters which the user guessed that are also in the correct word
        #for i in user_chars:
            #if i in word_chars:
                #print("The letter %s is correct!" % user_chars[i])

        if correct_chars > 0:
            print("%s/4 characters correct" % correct_chars)

        guesses = guesses + 1
       
       # if user goes over guess limit prompt to play again
        if guesses == 6:
            print(f'You were not able to guess the word, the word was "{random_word}"...')
            play_again()
            playing == False
        
    #print(user_chars)

def play_again():
    play_again = input("Play again? y/n ")
    if play_again == "y":
        playing == True
    
    else:
        quit()

while playing:
    guess()