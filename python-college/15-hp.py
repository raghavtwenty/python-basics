''' Q3
Write a program  to display the n terms of harmonic series and their
sum. 
1 + 1/2 + 1/3 + 1/4 + 1/5 ... 1/n terms

Test Data : 
Input the number of terms : 5 

1/1 + 1/2 + 1/3 + 1/4 + 1/5 +
Sum of Series upto 5 terms : 2.283334'''

import math

print('\nSum Of Harmonic Progression\n')
count = int(input('Enter The Denominator Of The Last Term: '))
stri = ''
for i in range(count+1):
    if i!=0:
        stri += f'1/{i} + '

print(stri[:-2])
# a = 1 & d = 1
#sn = 1/d ln (2a+(2n-1)d)/2a-d
cc = (2*count-1)/1
sumhp = math.log (2+cc)
print(f'Sum Of All HP: {sumhp}')
