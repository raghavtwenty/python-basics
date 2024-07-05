"""
Filename: _0012_chaining_operators.py
Title: Chaining operators in python 
Author: Raghava | GitHub : @raghavtwenty
Date Created: July 5, 2024 | Last Updated: July 5, 2024
Language: Python | Version: 3.12.3, 64-bit
"""

# = equal to
# != not equal to

# Integer checking
x = 10
print(1 < x < 20)  
print(10 < x < 20) 
print(x < 20 > 15) 

x = 10
y = 20
z = 30

# Check if x is less than y and y is less than or equal to z
print(x < y and y <= z)  # Output: True

# Check if x is not equal to y and (y is greater than z or x is less than z)
print(x != y and (y > z or x < z))  # Output: True

# Check if x is less than y and y is less than z, and also if x is not equal to z
print(x < y < z and x != z)  # Output: True


# List checking
a = [1, 2, 3]
b = a
c = [1, 2, 3]

# Check if b is a and a is not c
print(b is a is not c)  # Output: True

# Check if 1 is in a and 2 is in a
print(1 in a and 2 in a)  # Output: True

# Check if 4 is not in a and a is not c
print(4 not in a and a is not c)  # Output: True



