import json
import random

with open('4_letter_words.json', 'r') as file:
    words_data = json.load(file)

words_list = [entry['word'] for entry in words_data]

random_word = random.choice(words_list)
print(random_word)