''' Q2.
Write a  program to prompt the user to input 3 integer values and 
print these values in forward and reversed order. '''

# Date Created : 17-11-2021 | Date Edited : 17-11-2021

print('\nForward and Reverse Order of Numbers.\n')
lst = []
for i in range(3):
	a = int(input(f'Enter The {i}th Number: '))
	lst.append(a)

lst_r = reversed(lst)

print('\nForward Order: ')
for i in lst:
	print(i)

print('\nReverse Order: ')
for i in lst_r:
	print(i)