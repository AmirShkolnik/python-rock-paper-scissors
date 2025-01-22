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
game_symbols = [rock, paper, scissors]
user_choice = int(input('What do you choose?\n'
                    'Type 0 for Rock, 1 for Paper,'
                    '2 for Scissors.\n'))
if user_choice in [0, 1, 2]:
    print(f'You chose : {user_choice}')
    print(game_symbols[user_choice])
    computer_choice = random.randint(0, 2)
    print(f'Computer chose: {computer_choice}')
    print(game_symbols[computer_choice])
    if computer_choice == user_choice:
        print("It's a draw")
    elif (user_choice == 0 and computer_choice == 2) or \
    (user_choice == 1 and computer_choice == 0) or \
    (user_choice == 2 and computer_choice == 1):
        print("You Win!")
    else:
        print("You Lose!")
else:
    print("You typed an invalid number. You lose!")
