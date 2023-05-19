"""
Q44. Write a program that keeps student's name and his marks in a dictionary 
as key-value pairs. The program should store records of 10 students and display 
students name and marks of five students in decreasing order of marks obtained.
                        author @raghav
Date Created : 30 Dec 2021 | Last Updated : 30 Dec 2021
"""


# Main
print('\nStudents Mark List.\n')

dictionary = dict()
for i in range(10) :       # Inserting data into dictionary
    name = str(input(f'Enter The Name Of Student {i}: '))
    mark = int(input(f'Enter The Total Marks Secured By {name}: '))
    dictionary[name] = mark


print("\nTop 5 Students.")

sorted_rev = sorted(dictionary.items(), key = lambda x : x[1], reverse = True)
# Sort by entire dictionary | key to specify the sort by value type, [1] -> value| then reverse it.

count = 1       # Initialization
for i in sorted_rev:
    if count <= 5:      # Top 5
        print(f'Rank : {count} | Name : {i[0]} | Mark : {i[1]}')        # Show
    count += 1

    
