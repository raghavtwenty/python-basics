''' Q1. 
Write a Python program to get a string made of the first 2 and 
the last 2 chars from a given a string. If the string length is less 
than 2, return instead of the empty string. 

Input Format:
The first line of the input contains the String S. 
Output Format:
The first line of the output contains the modified string. 
             
Sample Input:
Programming
Sample Output:
Prng
'''

print('\nFirst And Last Two Character.\n')
string = str(input('Enter The String: '))
if len(string)>=2:
    print(string[0],string[1],string[-2],string[-1])
else:
    print('\nString Length Is Less Than Two Character.')