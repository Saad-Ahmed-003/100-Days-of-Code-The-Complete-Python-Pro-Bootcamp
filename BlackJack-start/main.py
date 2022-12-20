import random\

List = [11, 2, 3, 4, 5, 6 ,7, 8 ,9, 10, 10, 10, 10]

my_card = []
computer = []
repeat = True
num2 = 0

# get computer close to 21 function
def get_computerTo21():
    num = 0
    num1 = 0
    Computer = True
    while Computer == True:
        computer.append(random.choice(List))
        for i in computer:
            num += 1
        if num > 2:
            if sum(computer) > 21:
                if 11 in computer:
                    num1 = computer.index(11)
                    computer.remove(11)
                    computer.insert(num1, 1)
                    Computer = False
                else:
                    computer.pop(num-1)
                    Computer = False
        num = 0


def get_11_to_1 ():
    if 11 in my_card:
        if sum(my_card) > 21 :
            num = my_card.index(11)
            my_card.remove(11)
            my_card.insert(num, 1)


def check_the_Answer(list1, list2, option):
    if option == 1:
        if sum(list1) > 21:
            print(f"   Your final hand: {list1}, final score: {sum(list1)}")
            print(f"   Computer's final hand: {list2}, final score: {sum(list2)}")
            print("You went over. You lose")
            repeat = False
            
    elif option == 2:
        if sum(list1) > 21:
            print(f"   Your final hand: {list1}, final score: {sum(list1)}")
            print(f"   Computer's final hand: {list2}, final score: {sum(list2)}")
            print("You went over. You lose")
            repeat = False
        elif sum(list1) < sum(list2):
            print(f"   Your final hand: {list1}, final score: {sum(list1)}")
            print(f"   Computer's final hand: {list2}, final score: {sum(list2)}")
            print("You lose")
            repeat = False
        elif sum(list1) <= 21:
            if sum(list1) == sum(list2):
                print("Draw")
                repeat = False
            else:
                print("You win")
                repeat = False


#get 2 sets of 2 randome cards
for i in range(2):
    my_card.append(random.choice(List))
    computer.append(random.choice(List))

print(my_card, computer)


print(f"   Your cards: {my_card}, current score: {sum(my_card)}")
print|(f"   Computer's first card: {computer[0]}")
Continue = input("Type 'y' to get another card, type 'n' to pass:")

if Continue == "y":
    while repeat == True:
        my_card.append(random.choice(List))
        get_11_to_1()
        print(f"   Your cards: {my_card}, current score: {sum(my_card)}")
        print(f"   Computer's first card: {computer[0]}")
        check_the_Answer(my_card, computer, 1)
        Continue1 = input("Type 'y' to get another card, type 'n' to pass:")
        if Continue1 == "n":
            check_the_Answer(my_card, computer, 2)

