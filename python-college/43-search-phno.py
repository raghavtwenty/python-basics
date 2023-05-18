"""
Q43. Write a Python program to input n names and phone numbers to store it in 
a dictionary and print the phone number of a particular name.
                        author @raghav
Date Created : 30 Dec 2021 | Last Updated : 30 Dec 2021
"""


# Main
print('\nProgram To Search Customer\'s Details By Phone Number.\n')

dictionary = dict()
number = int(input('Enter Total Customer Count: '))
for i in range(number) :       # Inserting data into dictionary
    ph_no = int(input(f'Enter The Phone Number Of The Customer {i}: '))
    name = str(input('Enter The Name Of The Customer: '))
    dictionary[ph_no] = name

del_num = int(input('\nEnter The Phone Number To Be Searched: '))
for j,k in dictionary.items() :       # Iterating all data
        if j == del_num:        # Match with phone number
            print(f'{j} : {k}')


