'''Simple Programs --- Q1.     
Write a program that
requests three floating point numbers, and prints their sum and product.'''
# Date Created : 11-11-2021 | Date Edited : 11-11-2021

i = 0
Sum = 0
Product = 1
while i<3:
	a = float(input(f'\nEnter {i}th number value: ')) # User Input
	Sum += a
	Product *= a
	i += 1

print(f'\nSum: {Sum} and Product: {Product}\n')