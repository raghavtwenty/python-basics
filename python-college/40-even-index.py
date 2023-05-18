"""
Q40. Return the values of the elements at even index positions
                        author @raghav
Date Created : 23 Dec 2021 | Last Updated : 23 Dec 2021
"""


# Functions
def evenpositions(l):
    lst00 = [ ]
    for i in range(len(l)):
        if i%2==0:
            lst00.append(l[i])
    
    print(lst00)


# Main
print("\nReturns The Values Of The Elements At Even Index Positions.\n")

lst = str(input("Enter The List Of Elements: "))
lst = lst.split(",")

evenpositions(lst)