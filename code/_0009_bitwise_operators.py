"""
Filename: _0009_bitwise_operators.py
Title: Logical operators in python
Author: Raghava | GitHub : @raghavtwenty
Date Created: July 4, 2024 | Last Updated: July 4, 2024
Language: Python | Version: 3.12.3, 64-bit
"""

a = 10  # In binary: 1010
b = 4   # In binary: 0100

# Bitwise AND
print(a & b)  # Output: 0 (0000)

# Bitwise OR
print(a | b)  # Output: 14 (1110)

# Bitwise XOR
print(a ^ b)  # Output: 14 (1110)

# Bitwise NOT
print(~a)  # Output: -11 (Two's complement: 10101)

# Bitwise left shift
print(a << 1)  # Output: 20 (10100)

# Bitwise right shift
print(a >> 1)  # Output: 5 (0101)
