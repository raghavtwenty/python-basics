# -*- coding: utf-8 -*-
"""
Created on Sat Sep 28 14:23:51 2019

@author: raghav 
"""


# 29 sept 2019
print('program to find quotient,sum,difference,and product')
n1 = int(input('enter the number: '))
n2 = int(input('enter the number: '))
try:
    q = n1/n2
    print('quotient=', q)
except:
    print("denominator cannot be zero")
