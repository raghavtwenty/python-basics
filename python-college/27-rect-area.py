''' Q2.Write a function that computes the area of a rectangle. 
Then, write a second function that calls this function three times 
to compute the surface area of a rectangular solid.'''

print('\nArea Of Rectangle.\n')

def rect(l,b):

	global ARR, lb
	lb = l*b
	ARR = f'Area Of Rectangle: {lb}'
	return ARR

def three():
	count = 0
	for i in range(3):
		rect(l,b)
		count+=lb
	print(f'Surface Area Of A Rectangular Solid: {2*count}')


l = int(input('Enter The Length: '))
b = int(input('Enter The Breadth: '))

print(rect(l,b))
three()