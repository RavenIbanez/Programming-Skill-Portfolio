# -*- coding: utf-8 -*-
"""
Created on Sun Oct 20 23:58:13 2024

@author: Royal
"""

month_days = { #  same as the other one, key:value dictionary so its easier and faster
    1: 31,  
    2: 28,  
    3: 31,  
    4: 30,  
    5: 31,  
    6: 30,  
    7: 31,  
    8: 31,  
    9: 30,  
    10: 31, 
    11: 30,
    12: 31  
}

try: # have an input for month and year
    month = int(input("Month (1-12): "))# would be cooler if i had it detect both text and number, but I'll stick with this 
    year = int(input("Year: "))
    
    if 1 <= month <= 12:
       
        if month == 2: #now we check for february, this is for the advanced requirement
      # wouldve been easier if i was asking if it was a leap year or not, but what if the person doesn't know what a leap year is?
            if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0): # using leap year math here; leap years are divisble by 4 but not by 100, but divisible by 400
                print(f"February {year} has 29 days.")
            else:
                print(f"February {year} has 28 days.")
        else:
            print(f"The month has {month_days[month]} days.")# if the month is not feb, it would go here directly
    else:
        print("Invalid month number. Please enter a number between 1 and 12.") # just incase someone puts the word and not the number of the month -_-

except ValueError:
    print("Invalid input. Please enter valid numbers for the month and year.")