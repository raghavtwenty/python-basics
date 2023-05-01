'''Simple Programs --- Q3.     
Two persons are standing apart by 1m, each has a mass of 50kg. 
Let G=6.67x10-11Nm2/kg2 and rearth=6.64x106m. Determine the force of
F gravitation between P1 and P2. How many times should F be multiplied to get
the force of gravitation between the Earth and P1.'''
# Date Created : 14-11-2021 | Date Edited : 14-11-2021

P1 = float(input('\nEnter The Mass Of 1st Object: '))
P2 = float(input('Enter The Mass Of 2st Object: '))
D = float(input('Enter Distance (M) Between Object 1 & 2: '))

# F = G*p1*p2/r**2 --- Formula

# Object 1 & 2
G = 6.67*10**-11
F = G*P1*P2/D
print(f'\n{F} N, Is The Force Of Gravitation Between Object 1 & 2.')

# Object 1 & Earth
Mass_Earth = 5.97219*10**24
RE_F = G*P1*Mass_Earth/D
print(f'\n{RE_F} N, Is The Force Of Gravitation Between Object 1 & Earth.')

Multi_Factor = RE_F/F 
print(f'''\nF Should Be Multiplied {Multi_Factor} Times To Get, 
Force Of Gravitation Between Earth And Object 1.\n''')

