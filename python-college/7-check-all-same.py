''' Q4.
Write a program that accepts three integers from the keyboard. 
It prints out number 1 if any two of them (or all of them) are equal and 
prints out zero if all of them are different. '''

# Date Created : 17-11-2021 | Date Edited : 17-11-2021

print('\nCheck Same Numbers Or Not.\n')
lst = []
for i in range(3):
	num = int(input(f'Enter {i}th Number: '))
	lst.append(num)

if lst[0]==lst[1]==lst[2] or lst[0]==lst[1] or lst[1]==lst[2] or lst[2]==lst[1]:
	print('\n1')
else:
	print('\n0')



