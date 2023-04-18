# -*- coding: utf-8 -*-
"""
Created on Tue Aug 27 11:01:42 2019

@author: User
"""

#27 aug 2019
#raghav 11 c 
perc=int(input('enter the percentage:   '))
if perc>=85:
    grade ='A'
    print('KEEP IT UP')
elif perc>70 and perc<85:
    grade='B'
elif perc>60 and perc<=70:
    grade='C'  
elif perc>40 and perc<=60:
    grade='D'
else:
    grade='E'
print ('THE GRADE SECURED=', grade)     
