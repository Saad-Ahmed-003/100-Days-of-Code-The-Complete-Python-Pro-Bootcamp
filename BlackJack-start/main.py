import random

List = [11, 2, 3, 4, 5, 6 ,7, 8 ,9, 10, 10, 10, 10]

my_card = []
computer = []




for i in range(2):
    my_card.append(random.choice(List))
    computer.append(random.choice(List))

print(my_card, computer)

def get_computerTo21():
    num = 0
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
                computer.pop(num-1)
                print(computer)
                Computer = False
        num = 0
        print(num)

def check_the_Answer(list1, list2, option):
    if option == 1:
        if list1 > 21:
            print(f"   Your final hand: {list1}, final score: {sum(list1)}")
            print(f"   Computer's final hand: {list2}, final score: {sum(list2)}")
            print("You went over. You lose")
    elif option == 2:
        if sum(list1) > 21:
            print(f"   Your final hand: {list1}, final score: {sum(list1)}")
            print(f"   Computer's final hand: {list2}, final score: {sum(list2)}")
            print("You went over. You lose")
        elif sum(list1) < sum(list2):
            print(f"   Your final hand: {list1}, final score: {sum(list1)}")
            print(f"   Computer's final hand: {list2}, final score: {sum(list2)}")
            print("You lose")




print(f"   Your cards: {my_card}, current score: {sum(my_card)}")
print(f"   Computer's first card: {computer[0]}")
check_the_Answer(my_card, computer, 1)
Continue = input("Type 'y' to get another card, type 'n' to pass: ")

if Continue.lower() == "n":
    get_computerTo21()
    print(sum(computer))
    check_the_Answer(list1=my_card, list2=computer, option=2)
    


