from replit import clear
import art
#HINT: You can call clear() to clear the output in the console.
print(art.logo)
print("Welcome to the secret auction program.")


auction_data = {}
bid_data = []
num = 0
tru_fals = False


def add_data_to_auction(bider_Name, bider_bid):
    auction_data[str(bider_bid)] = bider_Name

while tru_fals == False:
    name = input("What is your name?: ")
    bid = input("What's your bid?: ")
    Continue = input("Are there any other bidders? Type 'yes' or 'no'.\n")
    add_data_to_auction(bider_Name=name, bider_bid=bid)
    if Continue == "no":
      tru_fals = True
    elif Continue == "yes":
      clear()
      tru_fals = False


for i in auction_data:
    if num < int(i):
        num = int(i)

clear()
print(f'The winner is {auction_data[str(num)]} with a bid of ${num}')

