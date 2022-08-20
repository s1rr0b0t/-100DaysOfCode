#Step 1 
import random
from re import search



word_list = ["aardvark", "baboon", "camel"]

#TODO-1 - Randomly choose a word from the word_list and assign it to a variable called chosen_word.

#TODO-2 - Ask the user to guess a letter and assign their answer to a variable called guess. Make guess lowercase.

#TODO-3 - Check if the letter the user guessed (guess) is one of the letters in the chosen_word.

random_word = list(random.choice(word_list))

tmp_random_word = random_word.copy()

print(random_word)

word = []

for x in range(0, len(random_word)):
    word.append('_')

print(word)

intentos = 0
while(intentos < 5):
    if '_' in word:
        letter_by_user = input("Input a letter: ")
        x = 0
        while( x < len(random_word)):
            if letter_by_user == random_word[x]:
                word[x] = letter_by_user
            x+=1
        print(f"Try number: {intentos+1} - Word: {word}")
    else:
        break
    intentos += 1

