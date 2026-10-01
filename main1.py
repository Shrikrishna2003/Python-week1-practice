from student_result import *
name = input("Enter student's name: ")
roll_no = input("Enter roll number: ")

m1 = float(input("Enter marks for Subject 1: "))
m2 = float(input("Enter marks for Subject 2: "))
m3 = float(input("Enter marks for Subject 3: "))

student_details(name, roll_no)

total = calculate_total(m1, m2, m3)
print("Total Marks:", total)

average = calculate_average(total)
print("Average Marks:", average)

result = get_result(average)
print("Result:", result)

grade = show_grade(average)
print("Grade:", grade)