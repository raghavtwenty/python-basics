"""
Filename: _0010_membership_operators.py
Title: Membership operators in python
Author: Raghava | GitHub : @raghavtwenty
Date Created: July 5, 2024 | Last Updated: July 5, 2024
Language: Python | Version: 3.12.3, 64-bit
"""

# List membership
lst = [1, 2, 3, 4, 5]
print(6 not in lst)  
print(3 in lst)  

# String membership
string = "hello"
print('z' not in string)  
print('h' in string)  

# Tuple membership
tup = (1, 2, 3)
print(4 in tup)  
print(2 in tup)  

# Dictionary membership (checks keys)
dct = {'a': 1, 'b': 2}
print('a' in dct)  
print('b' not in dct)   
