"""
Q47. Write a program to remove an empty tuple from a given list of tuples.
                        author @raghav
Date Created : 30 Dec 2021 | Last Updated : 8 Jan 2022
"""


# Main
print('\nProgram To Remove Empty Tuples.\n')

tuples = [('','','8'), (), ('0', '00', '000'),  ('birbal', '', '45'), (''), (),  ('',''),()]

print('Before Removing Empty Tuples : ')
print(tuples)

print("After Removing Empty Elements : ")
for i in tuples :       # 1st iteration for original tuples
    for j in i :        # Iteration for nested tuples
        if type(j) != None :        # Check by None type
            print(i, end=", ")
            break
print()
