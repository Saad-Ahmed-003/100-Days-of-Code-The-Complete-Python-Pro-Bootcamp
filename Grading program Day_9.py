student_scores = {
  "Harry": 81,
  "Ron": 78,
  "Hermione": 99, 
  "Draco": 74,
  "Neville": 62,
}
# 🚨 Don't change the code above 👆

#TODO-1: Create an empty dictionary called student_grades.

student_grades = {}

#TODO-2: Write your code below to add the grades to student_grades.👇
x = 0

for i in student_scores:
    x = student_scores[i]
    if x > 90:
        student_grades[i]  = "Outstanding"
    elif x < 90 and x > 80 :
        student_grades[i] = "Exceeds Expectations"
    elif x < 80 and x > 70:
        student_grades[i] = "Acceptable"
    elif x < 70 :
        student_grades[i] = "Fail"
    

# 🚨 Don't change the code below 👇
print(student_grades)