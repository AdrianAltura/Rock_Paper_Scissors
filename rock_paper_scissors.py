import random

paper = """
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
"""

rock = """
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
"""

scissors = """
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
"""

# 0 = rock, 1 = paper, 2 = scissors

choices = [rock,paper,scissors]
computer = random.randint(0,2)
user = int(input('What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors\n'))

if user > 2:
  print('Invalid Entry. Try again!')

elif (user == 0 and computer == 2) or (user == 1 and computer == 0) or (user == 2 and computer == 1):
  print(choices[user])
  print('Computer chose:')
  print(choices[computer])
  print('You won')

elif user == computer:
  print(choices[user])
  print('Computer chose:')
  print(choices[computer])
  print("It's a tie")

elif user != computer:
  print(choices[user])
  print('Computer chose:')
  print(choices[computer])
  print("You lose")


  
