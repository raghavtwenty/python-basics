''' Q5. 
Write a program that takes a positive integer argument representing a 
calendar year and returns integer 1 if it is a leap year else 0. 
[Hint. A year is a leap year if (i) it is divisible by 4 but not divisible by 100 
or (ii) divisible by 400.] '''

# Date Created : 17-11-2021 | Date Edited : 17-11-2021

print('Leap Year or Not.\n')
year = int(input('Enter A Calendar Year: '))
if (year % 4 == 0) and (year % 100 != 0) or (year % 400 == 0):
	print(f'{year}, Is A Leap Year.')
else:
	print(f'{year}, Is Not A Leap Year.')
