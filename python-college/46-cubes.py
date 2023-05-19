"""
Q46. Given a positive integer number n, you have to write a program that 
generates a dictionary d which contains (i, i*i*i) such that i is the key and i*i*i is its value,
where i is from 1 to n (both included). Then you have to just print this dictionary d.
                        author @raghav
Date Created : 30 Dec 2021 | 30 Dec 2021
"""


# Main 
print('\nInteger And It\'s Cube\n')

d = {}
num = int(input('Enter The Number: '))
for i in range(1, num+1):
    d[i] = pow(i,3)

print(d)