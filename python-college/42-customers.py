"""
Q42. Write a code to create customers list with their number & name and delete 
any particular customer using his /her number.
                        author @raghav
Date Created : 30 Dec 2021 | Last Updated : 30 Dec 2021
"""


# Functions
def dict_show():
    for j,k in dictionary.items() :       # Displaying all data
        print(f'{j} : {k}')


# Main
print('\nProgram To Create Customer\'s Details.\n')

dictionary = dict()
number = int(input('Enter Total Customer Count: '))
for i in range(number) :       # Inserting data into dictionary
    ph_no = int(input(f'Enter The Phone Number Of The Customer {i}: '))
    name = str(input('Enter The Name Of The Customer: '))
    dictionary[ph_no] = name

print('\nContents In The Dictionary.')
dict_show()     # Function call 

del_num = int(input('\nEnter The Phone Number To Delete Customer Data: '))
dictionary.pop(del_num)     # Removing item

print('\nDictionary After Deletion.')
dict_show()     # Function call 

