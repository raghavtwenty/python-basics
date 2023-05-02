'''Simple Programs --- Q4.     
How many molecules of H2O are present in 1 gm of snowflakes? Avogadro
number=6.022x1023, and atomic mass of H=1.01 and that of O=15.9994.'''
# Date Created : 14-11-2021 | Date Edited : 14-11-2021

SnowFlakes = float(input('\nEnter, How Many MilliGram (mg) Of Snowflakes: '))
SF_Conversion = SnowFlakes*1000
H20 = 18.02
Avogadro_Num = 6.022*10**23
ONEG_H20 = Avogadro_Num/H20

print(f'\nNumber Of H20 Molecules In 1g Of H20: {ONEG_H20}.')

SnowFlakes_Gram = ONEG_H20/SF_Conversion
print(f'\nSnowflakes Weighing {SnowFlakes} mg OF H2O: {SnowFlakes_Gram}')


