import random


rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

#Write your code below this line 👇
hand = [rock, paper, scissors]


choose_user = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors: "))

if choose_user >= 0 and choose_user <= 2:
    
    print(f"User chose: {hand[choose_user]}\n")
    choose_ram_pc = random.randint(0, 2)
    print(f"PC chose: {hand[choose_ram_pc]}\n")

    print("Result:\n")

    if choose_user == choose_ram_pc:
        print("DRAW")
    elif choose_user == 0 and choose_ram_pc == 2:
        print("YOU WIN!!")
    elif choose_user == 1 and choose_ram_pc == 0:
        print("YOU WIN!!")
    elif choose_user == 2 and choose_ram_pc == 1:
        print("YOU WIN!!")
    else:
        print("YOU LOSE!!")


else:
    print(f"You type invalid number[{choose_user}]... You Lose!")

     

