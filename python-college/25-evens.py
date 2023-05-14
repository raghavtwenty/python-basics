'''Q1.
Generate a Python list of all the even numbers between 4 to 30 
using an user defined function.'''

print('\nEven Numbers From 4 To 30.')

def evens(x):
	if x%2==0:
		print(x, end=' ')

for i in range(3,31):
	evens(i)
