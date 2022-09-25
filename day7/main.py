import random
import hangman_words
import hangman_art


def add_word(letter_by_user):
    x=0
    while( x < len(random_word)):
        if letter_by_user == random_word[x]:
            word[x] = letter_by_user
        x+=1


random_word = list(random.choice(hangman_words.word_list))
word = []

#Make a template empty with the spaces necesary to put letters.
for x in range(0, len(random_word)):
    word.append('_')

print(word)
print(random_word)
attemp = 1 # this variable start the count numbers of attemps
print(hangman_art.HANGMANPICS[0]) #Drawn hangman, use template 0. represent the beginning game
while(attemp <= 7 ):
# While exit this simbol '_' in word list the game to be continue...
    if '_' in word:
        if attemp == 7:
            break
        letter_by_user = input("Input letter: ").lower()
        if letter_by_user in random_word:
            if letter_by_user not in word:
                add_word(letter_by_user)
                print(f"Word: {word}")
        else:
            print(hangman_art.HANGMANPICS[attemp])
            print(f"Word: {word}")
            attemp += 1            
    else:
        print("CONGRATULATIONS - YOU WIN!!!")
        break

