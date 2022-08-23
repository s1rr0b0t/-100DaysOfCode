#Step 1 
from ast import Not
import random

def drawn_hangman(t):
    HANGMANPICS = ['''
    +---+
    |   |
        |
        |
        |
        |
    =========''', '''
    +---+
    |   |
    O   |
        |
        |
        |
    =========''', '''
    +---+
    |   |
    O   |
    |   |
        |
        |
    =========''', '''
    +---+
    |   |
    O   |
   /|   |
        |
        |
    =========''', '''
    +---+
    |   |
    O   |
   /|\  |
        |
        |
    =========''', '''
    +---+
    |   |
    O   |
   /|\  |
   /    |
        |
    =========''', '''
    +---+
    |   |
    O   |  GAME OVER -  YOU ARE DEAD!!!
   /|\  |
   / \  |
        |
    =========''']
    print(HANGMANPICS[t])



def add_word(letter_by_user):
    x=0
    while( x < len(random_word)):
        if letter_by_user == random_word[x]:
            word[x] = letter_by_user
        x+=1




word_list = ["aardvark", "baboon", "camel"]

random_word = list(random.choice(word_list))
word = []

for x in range(0, len(random_word)):
    word.append('_')

print(word)

trys = 1
drawn_hangman(0)
while(trys <= 7 ):
    if '_' in word:
        if trys == 7:
            break
        letter_by_user = input("Input letter: ")
        if letter_by_user in random_word:
            if letter_by_user not in word:
                add_word(letter_by_user)
                print(f"Word: {word}")
        else:
            drawn_hangman(trys)
            print(f"Word: {word}")
            trys += 1            
    else:
        print("CONGRATULATIONS - YOU WIN!!!")
        break

