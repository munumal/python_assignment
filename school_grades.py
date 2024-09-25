# -*- coding: utf-8 -*-
"""
Created on Wed Sep 25 14:22:06 2024

@author: Musaddique
"""

def calculate_grades(student_grades):
    if not student_grades:
        return None, None, None  

    total = 0
    highest = student_grades[0][1]
    lowest = student_grades[0][1]

    for student, grade in student_grades:
        total += grade
        if grade > highest:
            highest = grade
        if grade < lowest:
            lowest = grade

    average = total / len(student_grades)
    return average, highest, lowest

#use case
students = [("Adi", 85), ("Godl", 92), ("Prakash", 78), ("Musa", 90)]
average, highest, lowest = calculate_grades(students)

print(f"Average Grade: {average}")
print(f"Highest Grade: {highest}")
print(f"Lowest Grade: {lowest}")
