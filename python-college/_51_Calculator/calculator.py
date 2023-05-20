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


# Functions

# Factorial 
def fact(n) :
    count = 1

    for i in range(n, 1, -1) :
        count *= i

    if n == 0 :
        count *= 1

    return count


# Fibonacci Series
def fib(n) :
    if n <= 1:
       return n
    else :
       return  fib(n-1) + fib(n-2)      # Recursion
