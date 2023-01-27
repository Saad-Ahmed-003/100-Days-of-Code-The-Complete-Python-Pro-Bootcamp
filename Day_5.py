import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v',
           'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R',
           'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")

nr_letters = int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input("How many symbols would you like?\n"))
nr_numbers = int(input("how many numbers would you like?\n"))

# Eazy level - Order not randomised:
# e.g. 4 letter, 2 symbol, 2 numbers = wedR#%46

password = ""

for i in range(nr_letters):
    data = random.choice(letters)
    password += data


for i in range(nr_symbols):
    data = random.choice(symbols)
    password += data

for i in range(nr_numbers):
    data = random.choice(numbers)
    password += data

print(password)

# Hard Level - Order of characters randomised:
# e.g. 4 letters, 2 symbol, 2 number = g^2jk8&P

hardPassword_list = []

hardPassword = ""

for i in range(nr_letters):
    data = random.choice(letters)
    hardPassword_list += data

for i in range(nr_symbols):
    data = random.choice(symbols)
    hardPassword_list += data

for i in range(nr_numbers):
    data = random.choice(numbers)
    hardPassword_list += data

random.shuffle(hardPassword_list)
for i in hardPassword_list:
    hardPassword += i

random.shuffle(hardPassword_list)
for i in hardPassword_list:
    hardPassword += i

print(hardPassword)
