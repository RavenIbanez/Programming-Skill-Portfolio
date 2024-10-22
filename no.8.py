# -*- coding: utf-8 -*-
"""
Created on Mon Oct 21 10:27:50 2024

@author: Royal
"""
 
names = ["Jake", "Zac", "Ian", "Ron", "Sam", "Dave"] # create a list for the names

search_term = input("Enter the name to search for: ").strip().lower() # get input, .strip and .lower would help just incase the user types it in all caps, adds spaces, etc

if search_term in [name.lower() for name in names]: # convert the names to lowercase to match
    print(f"'{search_term}' found in the list!")
else:
    print(f"'{search_term}' not found in the list.")

