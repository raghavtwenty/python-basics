''' Q4.
Write a program to display the sum of the series [ 9 + 99 + 999 + 9999...]. 
Test Data : 
Input the number or terms :5 
9 99 999 9999 99999 
The sum of the series = 111105'''

print('\nSum Of Series [ 9 + 99 + 999 + 9999...].\n')
count = int(input('Enter The Number Of Terms: '))
stri = ''
sum1 = 0
for i in range(count+1): #5
#i =2
    if i!=0:
        stri += '9'*i+' '   #9  #'9'x2=99
        ini = int('9'*i)
        sum1 += int('9'*i)   #9  #9x2 =18

print(stri)


#print(f'\nSum Of GP: {sumgp1}')
print(f'\nSum Of GP: {sum1}')









#print(stri)

# a(r^n-1)/r-1

#sumgp = (10**count-1)-count
#sumgp1 = 10/9*(sumgp)