''' Q3.
Write a program that asks a number and test the number whether 
it is multiple of 5 or not, divisible by 7 but not by eleven.'''

# Date Created : 14-11-2021 | Date Edited : 17-11-2021

print('\nCheck Entered Integer Is 5, 7, 11.\n')
try:
	Number = int(input("Enter A Integer Number To Check: "))

	# 5
	if Number % 5 == 0:
		print(f'\n{Number}, Is Multiple Of 5.')
	else:
		print(f'\n{Number}, Is Not Multiple Of 5.')

	# 7 & 11
	if Number % 7 == 0 and Number % 11 != 0:
		print(f'{Number}, Is Divisible By 7 And Not By 11.')
	elif Number % 7 == 0:
		print(f'{Number}, Is Divisible By 7 And 11.')

	else:
		print(f'{Number}, Is Not Divisible By 7 And 11.')

except:
	print(f'{Number} Is A Float Value.')

