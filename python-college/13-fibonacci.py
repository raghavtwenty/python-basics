'''8. Write a program to display the first terms n of 
Fibonacci series. Fibonacci series 0 1 2 3 5 8 13 ...'''

#Date created: 18 nov 2021 | last edited: 25 nov 2021

print('\nFibonacci Series\n')

def feb(n):	 # function creation
	if n==1:
		return 0  # return 0 if interator number =1
	elif n==2:
		return 1  # return 1 if interator number =2
	else:
		return feb(n-1)+feb(n-2)  #formula for fibonacci series

num = int(input('Enter Number Of Terms: '))
for i in range(1, num+1): #iteration through each term
	print(feb(i))	 #display to the user

'''
				Alternate Way
i = 1
lst = [0,1,1]
if num > 3:
	for i in range(1, num+1):
		 if i not in [1,2]:
		 	content = lst[-1] + lst[-2]
		 	lst.append(content)
	for j in lst:
	print(j, end = '')

elif num == 1:
	print('0')
elif num == 2:
	print('0,1')
elif num == 3:
	print('0,1,1')
else:
	print('NONE')
'''
