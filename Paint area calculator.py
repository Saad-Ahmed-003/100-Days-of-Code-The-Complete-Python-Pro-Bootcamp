#Write your code below this line 👇
import numpy as np

def paint_calc(height, width, cover):
    number_of_cans = (height * width) / cover
    NumberOfCans = np.ceil(number_of_cans)
    print(f'You\'ll need {int(NumberOfCans)} cans of paint.')





#Write your code above this line 👆
# Define a function called paint_calc() so that the code below works.   

# 🚨 Don't change the code below 👇
test_h = int(input("Height of wall: "))
test_w = int(input("Width of wall: "))
coverage = 5
paint_calc(height=test_h, width=test_w, cover=coverage)

