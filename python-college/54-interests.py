'''
54. Create a package in Python name Interest and within this package create two 
modules simple.py and compound.py. The simple.py module contains function 
Simple_Interest() and compound.py module contains function Compound_Interest(). 
                        author @raghav
Date Created : 7 Jan 2022 | Last Updated : 7 Jan 2022
'''


# Importing required libraries
from _54_interest import compound as ci
from _54_interest import simple as si

print('\nSimple Interest & Compound Interest In Modules.\n')

p = float(input('Enter The Principal Amount : '))
r = float(input('Enter The Rate Of Interest In % : '))
t = float(input('Enter The Time Period : '))

r = r/100
print(f'\nSimple Interest : {si.simple_interest(p, r, t)}')
print(f'\nCompund Interest (Annually): {ci.compound_interest(p, r, t)}')
