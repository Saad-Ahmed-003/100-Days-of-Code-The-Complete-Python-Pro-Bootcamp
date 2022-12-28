import random
from game_data import data
import art
num = 1
adata = True
win_counts = 0


for i in data:
    num += 1

variable = random.choice(range(num))
print(art.logo)
print("Compare A: " +data[variable]['name']+", " +data[variable]['description']+", " +data[variable]['country'], data[variable]['follower_count'] )

print(art.vs)

variable2 = random.randrange(0, num)
print("Against B: " +data[variable2]['name']+ ", "+data[variable2]['description']+", "+data[variable2]['country'], data[variable2]['follower_count'])
variable3 = input("Who has more followers? Type 'A' or 'B':")

if variable3.lower() == "a":
    if data[variable]['follower_count'] > data[variable2]['follower_count']:
        print("you win")
        win_counts += 1
    elif data[variable]['follower_count'] < data[variable2]['follower_count']:
        print("you loose")
        adata = False
elif variable3.lower() == "b":
    if data[variable]['follower_count'] < data[variable2]['follower_count']:
        print("you win")
        win_counts += 1
    elif data[variable]['follower_count'] > data[variable2]['follower_count']:
        print("you loose")
        adata = False



while adata == True:
    variable = random.choice(range(num))
    print(art.logo)
    print(f"You're right! Current score: {win_counts}.")
    print("Compare A: " +data[variable]['name']+", " +data[variable]['description']+", " +data[variable]['country'], data[variable]['follower_count'] )

    print(art.vs)

    variable2 = random.randrange(0, num)
    print("Against B: " +data[variable2]['name']+ ", "+data[variable2]['description']+", "+data[variable2]['country'], data[variable2]['follower_count'])
    variable3 = input("Who has more followers? Type 'A' or 'B':")

    if variable3.lower() == "a":
        if data[variable]['follower_count'] > data[variable2]['follower_count']:
            print("you win")
        elif data[variable]['follower_count'] < data[variable2]['follower_count']:
            print("you loose")
            adata = False
    elif variable3.lower() == "b":
        if data[variable]['follower_count'] < data[variable2]['follower_count']:
            print("you win")
        elif data[variable]['follower_count'] > data[variable2]['follower_count']:
            print("you loose")
            adata = False