'''
51. Develop a module named calculator.py in Python, which contain three
function factorial(n) : to find factorial of a number, Fibonacci(n): to
find Fibonacci series up to given number, n. Perform following tasks:
a) Import the developed module
b) call the functions available in the module
i) to generate Fibonacci series upto a number, and
ii) to determine factorial of a number entered by user 
                        author @raghav
Date Created : 7 Jan 2022 | Last Updated : 7 Jan 2022
'''


# Importing required libraries
from _51_Calculator import calculator


# Main
print('\nFactorial And Fibonacci Series Using Modules.\n')

num = int(input('Enter A Integer Value : '))

print(f'\nFactorial : {calculator.fact(num)}')

for i in range(num) :
    print(f'Fibonacci Series : {calculator.fib(i)}')