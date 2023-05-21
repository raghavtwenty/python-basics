'''
55. Write a python code to implement division by zero exception.
                        author @raghav
Date Created : 7 Jan 2022 | Last Updated : 7 Jan 2022
'''


print('\nExplicitly Print Zero Division Error.\n')
   
iter = int(input('Enter The Number Of Iterations : '))

for i in range(iter) :

    try :       # Integer check
        num1 = int(input("Enter The Numerator : "))
        num2 = int(input('Enter The Denominator : '))

        try :       # Zero check
            print(f'Division Result : {num1/num2}\n')

        except ZeroDivisionError :
            print('Division By Zero.\n')

    except ValueError:
        print('Integer / Float Value Expected.\n')
