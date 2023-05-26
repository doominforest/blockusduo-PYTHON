# -*- coding: utf-8 -*-
"""
Created on Thu May 25 16:35:21 2023

@author: erins
"""

#erin learning how to take inputs and print it
def givename():
    name = input("What is your name dear? ")
    print("Your Name is: "+name)
    confirmation = input("Confirm? Y/N ")
    if confirmation == "Y":
        return name
    elif confirmation == "N":
        return givename()
    else:
        print ("Invalid Input")
        return givename()

print("Hello, "+givename())

    
    