# type 0 for rock, 1 for paper and 2 for scissor
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
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
'''

scissor ='''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
# print(rock)
# print(scissor)
# print(paper)

game_images =[rock, paper, scissor]
user_choice = input("Please enter your choice, Type 0 for ROCK, 1 for PAPER and 2 for SCISSOR \n ")
user_choice = int(user_choice)
if user_choice < 0 or user_choice >=3:
    print("You have typed a invalid number, you lose!")
else:
    print(game_images[user_choice])
computer_choice = random.randint(0,2)
print("Computer choice")
print(game_images[computer_choice])


if user_choice == 0 and computer_choice == 2:
    print("You win!")
elif computer_choice == 0 and user_choice == 2:
    print("You lose!")    
elif user_choice == 1 and computer_choice == 2:
    print("You lose!")
elif user_choice == 2 and computer_choice == 1:
    print("You win!")
elif user_choice == 2 and computer_choice == 3:
    print("You lose!")
elif user_choice == 3 and computer_choice == 2:
    print("You win!")    
elif computer_choice == user_choice:
    print("You draw!")

