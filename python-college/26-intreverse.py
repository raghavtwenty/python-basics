''' Q4.
Write a function intreverse(n) that takes as input a positive integer n and 
returns the integer obtained by reversing the digits in n. 
Here are some examples of how your function should work.
>>> intreverse(783)
387
						author @raghava
Date Created : 25 Nov 2021 | Last Updated : 25 Nov 2021
'''

def intreverse(num):
	print(num[::-1])

print('\nIntreverse.\n')
num = input('Enter the Number: ')
intreverse(num)
