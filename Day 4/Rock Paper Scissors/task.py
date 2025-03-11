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


options = [rock, paper, scissors]

user_choice = int(input("Choose 0 for rock, 1 for paper and 2 for scissors: "))
if user_choice == 0:
    print(options[0])
elif user_choice == 1:
    print(options[1])
elif user_choice == 2:
    print(options[2])
else:
    print("invalid option")

computer_choice = random.choice(options)

if user_choice == 0 and computer_choice == rock:
    print("It's a draw")
elif user_choice == 0 and computer_choice == paper:
    print("you lose")
elif user_choice == 0 and computer_choice == scissors:
    print("you win")
elif user_choice == 1 and computer_choice == rock:
    print("you win")
elif user_choice == 1 and computer_choice == paper:
    print("It's a draw")
elif user_choice == 1 and computer_choice == scissors:
    print("you lose")
elif user_choice == 2 and computer_choice == rock:
    print("you lose")
elif user_choice == 2 and computer_choice == paper:
    print("you win")
elif user_choice == 2 and computer_choice == scissors:
    print("It's a draw")



print("computer chose", computer_choice)