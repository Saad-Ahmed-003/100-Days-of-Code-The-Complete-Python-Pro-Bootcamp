# Go to https://replit.com/@appbrewery/rock-paper-scissors-start?v=1
import random


gesture0 =  '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

gesture1 = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

gesture2 = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

list = [0, 1, 2]

InData = input("What do you choose? Type 0 for Rock, 1 for paper, 2 for scissors.")

if InData == 0:
    print(gesture0)
elif InData == 1:
    print(gesture1)
elif InData == 2:
    print(gesture2)


AI = random.randit(0, 1, 2)

print("Computer chose:")

if AI == 0:
    print(gesture0)
elif AI == 1:
    print(gesture1)
elif AI == 2:
    print(gesture2)

if InData == 0 and AI == 1:
    print("You lose")
elif InData == 2 and AI == 1:
    print("You win")
elif InData == 2 and AI == 0:
    print("You lose")
elif InData == 1 and AI == 0:
    print("You win")
elif InData == 1 and AI == 2:
    print("You lose")
elif InData == 0 and AI == 2:
    print("You win")