import random

List = [11, 2, 3, 4, 5, 6 ,7, 8 ,9, 10, 10, 10, 10]

my_card = []
computer = []
repeat = True


# get computer close to 21 function
def get_computerTo21():
    num = 0
    num1 = 0
    Computer = True
    while Computer == True:
        computer.append(random.choice(List))
        print(computer)
        for i in computer:
            num += 1
            print(num)
        if num > 2:
            print(num)
            if sum(computer) > 21:
                if 11 in computer:
                    num1 = computer.index(11)
                    computer.remove(11)
                    computer.insert(num1, 1)
                    computer.pop(num-1)
                    print(computer)
                    Computer = False
                else:
                    computer.pop(num-1)
                    print(computer)
                    Computer = False
        num = 0
        print(num)


def get_11_to_1 ():
    if 11 in my_card:
        if sum(my_card) > 21 :
            num = my_card.index(11)
            my_card.remove(11)
            my_card.insert(num, 1)


def check_the_Answer(list1, list2, option):
    if option == 1:
        if list1 > 21:
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


#get 2 sets of 2 randome cards
for i in range(2):
    my_card.append(random.choice(List))
    computer.append(random.choice(List))

print(my_card, computer)


while repeat == True:
    print(f"   Your cards: {my_card}, current score: {sum(my_card)}")
    print(f"   Computer's first card: {computer[0]}")
    check_the_Answer(my_card, computer, 1)
    check_the_Answer(list1=my_card, list2=computer, option=1) 
    Continue = input("Type 'y' to get another card, type 'n' to pass: ")
    #check the answer
    if Continue.lower() == "n":
        get_computerTo21()
        print(sum(computer))
        check_the_Answer(list1=my_card, list2=computer, option=2)
    elif Continue.lower() == "y":
        my_card.append(random.choice(List))
        get_computerTo21()
        get_11_to_1()



