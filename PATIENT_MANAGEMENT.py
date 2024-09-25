# -*- coding: utf-8 -*-
"""
Created on Wed Sep 25 13:51:01 2024

@author: Musaddique
"""

'''Create a dictionary where the keys are patient IDs, and the values are dictionaries 
containing the patient’s name, age, and disease. Write a function to display the details of a 
patient when given the patient’s ID. Modify the function to return a patient’s data as a tuple 
instead of printing it. '''


patients = {
    "P0001": {"name": "Aditya ", "age": 23, "disease": "Fractured Limb"},
    "P0002": {"name": "Gaudel", "age": 25, "disease": "Rashes"},
    "P0003": {"name": "Musa", "age": 24, "disease": "Cold"}
}


def get_patient_details(patient_id):
    if patient_id in patients:
        patient = patients[patient_id]
        return (patient["name"], patient["age"], patient["disease"])
    else:
        return None



#use case
patient_id =input("Enter Patient ID: ")
patient_details = get_patient_details(patient_id)
if patient_details:
    print(f"Patient Details:\n\t\t Name: {patient_details[0]} \n\t\t Age: {patient_details[1]}\n\t\t Disease: {patient_details[2]}")
else:
    print("Patient not found.")