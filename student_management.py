# -*- coding: utf-8 -*-
"""
Created on Mon Sep 23 20:23:33 2024

@author: Musaddique
"""



students = []

def add_student(student_id,name,grade):
    for student in students :
        if student['ID'] == student_id:
            print(f" student with ID : {student_id} already exists !!!")
            return
    new_student = {
        'ID' : student_id,
        'Name' : name,
        'Grade' : grade
        }     
   
    students.append(new_student)
    print(f"Student: {name} added successfully !!!")    
    
    
add_student(101,"Musa",'A')
add_student(102,"Adam",'B') 
add_student(103,"Polynomial",'C')
add_student(102,"Determinant",'D')   
