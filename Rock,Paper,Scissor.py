print("\t \t \t Name: Jay Surya \n\t \t \t USN: 1AY24AI048 \n\t \t \t Sec: M")

import random

choices = ("rock", "paper", "scissor") 
user_choice = input("Enter the user choice (rock, paper, scissor): ").lower()
computer_choice = random.choice(choices)
print("Computer chose:", computer_choice)

if user_choice not in choices:
    print("Invalid input!!")
elif user_choice == computer_choice:
    print("It's a tie!!")
elif (user_choice == 'rock' and computer_choice == 'scissor') or \
     (user_choice == 'paper' and computer_choice == 'rock') or \
     (user_choice == 'scissor' and computer_choice == 'paper'):
    print("You Win!!")
else:
    print("Computer Wins!")

