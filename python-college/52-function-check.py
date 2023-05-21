'''
52. Write a Python program to check if a function is a user-defined function or not. 
Use types.FunctionType, types.LambdaType()
                        author @raghav
Date Created : 7 Jan 2022 | Last Updated : 7 Jan 2022
'''


# Importing required libraries 
from types import FunctionType, LambdaType


# Functions
def hello():

    print('Inside hello Function.')

    tup = ('Hello', 'Hola', 'Hallo')
    [print(i) for i in tup]

    print('Back To Main Program.\n')


# Main
print('\nProgram To Check The Type Of The Function.\n')
hello()
print(f'hello Is A User Defined Function : {isinstance(hello, FunctionType)}')
print(f'hello Is A Lambda Function : {isinstance(hello, LambdaType)}')
print(f'range Is A User Defined Function : {isinstance(range, FunctionType)}')


