from art import logo
import random

ans = random.choice(range(1, 101))
turn_count = 0


print(logo)
print("Welcome the Number Guessing Game! ")
print("I'm thinking of a number between 1 and 100")
level = input("Chose a difficulty. Type 'easy' or 'hard': ")
if level == "easy":
    turn_count = 10
elif level == "hard":
    turn_count = 5

while turn_count > 0:
    print(f"You have {turn_count} attempts remaining to guess the number.")
    guess = int(input("Make a guess: "))
    if guess == ans:
        print(f"You got it! The answer was {ans}")
        break
    elif guess < ans:
        print("Too low")
    elif guess > ans:
        print("Too high")
    turn_count -= 1