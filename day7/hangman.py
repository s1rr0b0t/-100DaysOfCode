#Step 1 

from random import random
from secrets import choice
import random

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

letter_by_user = input("Input a letter: ")

index_list = []

for x in random_word:
    if letter_by_user == x:
        index_list.append(tmp_random_word.index(x))
        tmp_random_word.remove(x)

print(index_list)


""" 

tmp_random_word = random_word.copy()
word = []

for x in range(0, len(random_word)):
    word.append('_')

letter_by_user = input("Input a letter: ")

index_list = []

for x in random_word:
    if letter_by_user == x:
        index_list.append(tmp_random_word.index(x))
        tmp_random_word.remove(x)




print(random_word)
print(word)
print(index_list) """