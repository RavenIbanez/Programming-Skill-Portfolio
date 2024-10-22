# -*- coding: utf-8 -*-
"""
Created on Tue Oct 22 22:04:10 2024

@author: Royal
"""

def check_even_odd(number): # had to look this up on google, the check_even_odd function would help check if it is even or odd
    if number % 2 == 0: # checks if the number is divisible by 2
        return "Even"
    else:
        return "Odd"
    
def main(): # main would ask the user for an input and it would check if its even or odd through check_even_odd
        number = int(input("Enter a number: "))
        print(f"The number is {check_even_odd(number)}.")
        
if __name__ == "__main__":
        main() 
        

