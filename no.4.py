# -*- coding: utf-8 -*-
"""
Created on Tue Sep 17 11:05:46 2024

@author: Royal
"""

# have a basic input variable

name = input("Enter your Name: ") 
hometown = input("Enter your Hometown: ")

while True:
    try: # will keep trying until a given response is acceptable
        age = int(input("Enter your age: ")) 
        break # after being given a proper response it breaks the loop
    except ValueError:
        print("Invalid input for age. Please enter a valid number.") 

# dictionary to collect the information
person_info = {}
person_info['name'] = name
person_info['hometown'] = hometown
person_info['age'] = age
print(f"Name: {person_info['name']}\nHometown: {person_info['hometown']}\nAge: {person_info['age']}")   
# prints collected information
# the f allows us to directly emebed it into the string without the use of +
# /n creates a new line for printing, saw this on a youtube video