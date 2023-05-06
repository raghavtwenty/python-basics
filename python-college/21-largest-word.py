''' Q2. 
Write a program to print Largest and Smallest Word 
from a given sentence. If there are two or more words of same length
then the first one is considered.

Input : Problem Solving through Programming in C. 
Output: Largest Word is: Programming
		Smallest word is: C
'''

print('\nLargest And Smallest Word.\n')
string = str(input('Enter The String: '))
ssplit = string.split()

lar = max(ssplit, key = len)
small = min(ssplit, key = len)
print(f'\nThe Largest Word: {lar}')
print(f'The Smallest Word: {small}')