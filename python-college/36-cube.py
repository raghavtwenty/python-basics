"""
Q3. Square & Cube Numbers Using Lambda Function
                        author @raghav
Date Created : 10 Dec 2021 | Last Updated : 11 Dec 2021
"""


# Importing Required Libraries
from math import pow


# Main
print("\nSquare & Cube Of Integers From The Given List Using Lambda Function.\n")

# Get The Input
lst = str(input("Enter Integer Values With Comma: "))
split = lst.split(',')

# Square & Cube
for i in split:
    def fun(j, k): return pow(j, k)
    print(f"Square Of {int(i)} : {fun(int(i),2)}")
    print(f"Cube Of {int(i)} : {fun(int(i),3)}")
