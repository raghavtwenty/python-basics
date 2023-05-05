# Q6. Write a program to display Pascal's triangle.

print('\nPascal\'s Triangle.\n')

n = int(input('Enter The Number Of Rows: '))
for line in range(1, n+1):  
    c=1  
    print('  '*(n-line), end = ' ')
    for i in range(1, line + 1): 
        print(str(c).center(3), end = ' ') 
        c = int(c * (line - i) / i)
    print()

