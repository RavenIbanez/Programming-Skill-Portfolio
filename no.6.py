# -*- coding: utf-8 -*-
"""
Created on Mon Oct 21 00:16:47 2024

@author: Royal
"""

password = "12345" # the correct password

user_input = "" # a avariable to store the input

while user_input != password: # while will keep asking until the correct password is entered
    user_input = input("Enter the password: ")

    if user_input != password:
        print("ACCESS DENIED, try again.") # will deny access if the answer is incorrect

print("ACCESS GRANTED")# will  print if the  correct password is given