'''Simple Programs --- Q5.     
Calculate the mass of air in an automobile tire using following formula
PV=0.37m(T+460) Where  P=Pressure, poundes per square
inche (psi), V=Volume (cubic feet) and m=mass of air (pounds) and T=temperature
(degrees in Fahrenheit).'''
# Date Created : 14-11-2021 | Date Edited : 14-11-2021

# User Input
P = float(input('Enter the Pressure Count: '))
V = float(input('Enter the Volume Count: '))
T = float(input('Enter the Temperature Count: '))

# Condition to be Satisfied : PV=0.37m(T+460) And find 'm' = mass
# PV = NRT
# PV = 0.37m(T+460)
Numerator = P*V
Denominator = 0.37*(T+460) 
m = Numerator/Denominator
print(f'Mass Of The Air In The Automobile Tire: {m}')
