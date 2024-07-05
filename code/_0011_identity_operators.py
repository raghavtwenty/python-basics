"""
Filename: _0011_identity_operators.py
Title: Identity operators in python (Refers to memory address)
Author: Raghava | GitHub : @raghavtwenty
Date Created: July 5, 2024 | Last Updated: July 5, 2024
Language: Python | Version: 3.12.3, 64-bit
"""

a = [1, 2, 3]
b = a
c = [1, 2, 3]

print(a is b)  # Output: True (a and b refer to the same object)
print(a is c)  # Output: False (a and c are different objects with the same content)
print(a is not b)  # Output: False (a and b refer to the same object)
print(a is not c)  # Output: True (a and c are different objects with the same content)

# Checking with integers
x = 10
y = 10

print(x is y)  # Output: True (small integers are cached in Python, so they refer to the same object)
print(x is not y)  # Output: False (small integers are cached in Python, so they refer to the same object)

# Checking with strings
s1 = "hello"
s2 = "hello"

print(s1 is s2)  # Output: True (string literals are interned by Python)
print(s1 is not s2)  # Output: False (string literals are interned by Python)