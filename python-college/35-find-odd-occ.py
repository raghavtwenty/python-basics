"""
Q2. Find the number which occurs an odd number of times in a list using the lambda function.
                        author @raghav
Date Created : 10 Dec 2021 | Last Updated : 11 Dec 2021
"""

# Functions
count = lambda dup_lst: dup_lst.count(dup_lst[j]) 

# Main
print("\nFinding The Number Which Occurs Odd Number Of Times.\n")

# Get The Input
lst = str(input("Enter Integer Values With Comma: "))
split = lst.split(',')
print(split)

# Clean The Input To Only Integers
dup_lst = [ ]
for i in split:
    s = int(i)
    dup_lst.append(s)
print(dup_lst)

# Count The Entities
for j in range(len(dup_lst)+1):
    if count(dup_lst)%2==1:
        print(f"\n{dup_lst[j]} , Occurs Odd Number Of Times In The Given List.")
        break
