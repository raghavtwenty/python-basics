''' Q6.
Write a program to accept a, b and c (from the keyboard) of the quadratic equation 
ax^2+bx+c = 0 such that the condition b < a + c < 0 holds. 
If the condition does not hold, then the program terminates with a message 
“Wrong Input". It then ends the real root(s) and print. Note down the output with
(i) a = -4; b = -4; c = 3
(ii) a = 4; b = -4; c = -3
(iii) a = 0; b = -5; c = -4
(iv) a = -2; b = -3; c = 1 '''

# Date Created : 17-11-2021 | Date Edited : 17-11-2021

print('\nFind The Roots Of The Quadratic Equation.\n')
a = int(input('Enter An Integer Value For a th term: '))
b = int(input('Enter An Integer Value For b th term: '))
c = int(input('Enter An Integer Value For c th term: '))
tup = (a,b,c)
if not 0 in tup:
	if b < a+c < 0:
		d = (b**2-4*a*c)**(1/2)
		r1 = (-b+d)/(2*a)
		r2 = (-b-d)/(2*a)
		print(f'The Roots Are: {r1} And {r2}')

	else:
		print('Wrong Input.')
else:
	print('Division By Zero Not Possible.')