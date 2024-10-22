# -*- coding: utf-8 -*-
"""
Created on Tue Sep 17 22:51:36 2024

@author: Royal
"""
# a dictionary where it is paired, this is easier than making it one by one which is what i've seen my friends do
questions = { #  key:value
    "France": "Paris",
    "Germany": "Berlin",
    "Spain": "Madrid",
    "Italy": "Rome",
    "Portugal": "Lisbon",
    "Netherlands": "Amsterdam",
    "Belgium": "Brussels",
    "Austria": "Vienna",
    "Sweden": "Stockholm",
    "Denmark": "Copenhagen"
}
# keeps the score at 0
Score = 0

for country, capital in questions.items(): # would assign the key:value items in the dictionary
    answer = input(f"What is the capital of {country}? ").strip().lower() # strip would remove unwanted spaces, lower would force every letter to lowercase
    if answer == capital.lower():  # compares the user input with the capital
        print("Correct!")
        Score += 1  # increases the score by 1 if the answer is correct
    else:
        print(f"Wrong! The correct answer is {capital}.")
# the f allows us to directly emebed it into the string without the use of +
print(f"\nYou scored {Score} out of {len(questions)}!")