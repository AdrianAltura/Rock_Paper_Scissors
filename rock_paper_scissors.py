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
user = input('What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors\n')

if user.isalpha():
  print("Invalid Entry. You have entered a string of letters. Please read the instructions")

elif user.isnumeric():
  computer = random.randint(0,2)
  x = int(user)
  if x > 2:
    print('Invalid Entry. Number entered too large! Please read instructions')
  
  elif (x == 0 and computer == 2) or (x == 1 and computer == 0) or (x == 2 and computer == 1):
    print(choices[x])
    print('Computer chose:')
    print(choices[computer])
    print('You won')
  
  elif x == computer:
    print(choices[x])
    print('Computer chose:')
    print(choices[computer])
    print("It's a tie")
  
  elif user != computer:
    print(choices[x])
    print('Computer chose:')
    print(choices[computer])
    print("You lose")
  

  
