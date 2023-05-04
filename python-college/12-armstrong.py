''' Q7. 
Write a program to find the Armstrong number for a given range 
of number.
Test Data :
Input starting number of range: 1
Input ending number of range : 1000
Armstrong numbers in given range are: 1 153 370 371 407
'''

print('\nArmstrong Number\n')

snum = int(input('Enter The Starting Number: '))
enum = int(input('Enter The Ending Number: '))
ml = {}
for i in range(snum, enum+1):
	j = str(i)
	lst = []
	for ii in j:
		intstr = int(ii)
		lst.append(intstr**3)
	ml[i]=lst

for k in ml:
	if k == sum(ml[k]):
		print(k, end = ',')


	

