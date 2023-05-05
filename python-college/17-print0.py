''' Q1. 
You are given a positive integer N. You have to print N rows as follows. 
The first row consists of one 0, the second row 2 zeroes, and so on, 
until the Nth row, which consists of N zeroes.
Sample Test Cases
Test Case 1
Input 2

Output
0
00 '''
print('\nPrinting Zeros.\n')
num = int(input("Enter A Positive Integer: "))
for i in range(num+1):
	print('0'*i)
