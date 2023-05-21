'''
3. Write a Python program to construct a Decimal from a float and a Decimal 
from a string. Also represent the Decimal value as a tuple. Use decimal.Decimal
                        author @raghav
Date Created : 7 Jan 2022 | Last Updated : 7 Jan 2022
'''


# Importing required libraries
from decimal import Decimal


# Main
print('\nDecimal Conversion.\n') 

float_num = float(input('Enter The A Floating Point Value : '))
str_num = input('Enter A String Value Of Integer Type : ')

float_num = Decimal(float_num)
str_num = Decimal(str_num)

print(f'\nFloating Point To Decimal Value : {float_num}')
print(f'In Terms Of Tuple : {float_num.as_tuple()}')
print(f'\nString To Decimal Value : {str_num}')
print(f'In Terms Of Tuple : {str_num.as_tuple()}')


