''' Q2.
Write a program to find the sum of the series [ 1-X^2/2!+X^4/4!- ......].
Test Data :
Input the Value of x :2
Input the number of terms : 5

the sum = -0.415873
Number of terms = 5
value of x = 2.000000'''


def Series(x, n):
	sum = 1
	term = 1
	fct = 1
	p = 1
	multi = 1
	

	for i in range(1, n):   # 5  #1 
		fct = fct * multi * (multi+1)  # 1*1*(1+1) = 2
		p = p*x*x  #1*2*2 = 4
		term = (-1) * term   # -1*1 = -1
		multi += 2 # multi = multi +1 === 1+1====>2
		sum = sum + (term * p)/fct   # 1+(-1*4)/2
		
	print(f'\nSum Of The Series: {sum}')
	print(f'Number Of Terms: {n}')
	print(f'Value Of X: {x}')


print('\nSum Of The Series [ 1-X^2/2!+X^4/4!- ......]\n')
x = int(input('Enter The Value Of X: '))
n = int(input('Enter The Number Of Terms: '))
Series(x, n)



