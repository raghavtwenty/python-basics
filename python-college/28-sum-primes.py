'''Q3. 
Write a function sumprimes(l) that takes as input a list of 
integers l and returns the sum of all the prime numbers in l.
Here are some examples to show how your function should work.
>>> sumprimes([3,3,1,13])
19
'''

print('\nSum Of Prime Numbers In A List.\n')

def sumprimes(lst):
	global sum_lst

	def sp(n):
		prime = 0
		for i in range(2, n):
			if (n%i == 0):
				prime = 1
		if (prime == 0):
			sum_lst.append(n)

	sum_lst = []
	for n in lst:
		sp(n)
		

lst = []
total_count = int(input('Enter Number Contents In The List: '))
for i in range(total_count):
	list_con = int(input(f'Enter {i}th Content: '))
	if list_con>1:
		lst.append(list_con)

sumprimes(lst)
print(f'Prime Numbers: {sum_lst}')
print(f'Sum Of Prime Numbers: {sum(sum_lst)}')

    




