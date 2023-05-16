"""
Q4. Possible outcomes of a dice
                        author @raghav
Date Created : 16 Dec 2021 | Last Updated : 16 Dec 2021
"""


# Importing Required Libraries
import random


# Functions
def roll_D(nof_dice, max=6):
    for i in range(nof_dice):
        print(f"Outcome In Die {i+1} : {random.randint(1,max)}")
    
    return "That\"s All"


# Main
print("\nPossible Outcomes Of Dices.\n")
nof_dice = int(input("Enter Number Of Dice: "))
print(roll_D(nof_dice))


