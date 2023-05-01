'''Simple Programs --- 2.     
Suppose an object is
thrown up with initial velocity of 50m/sec. How height the object will rise and
what time does it take to reach the highest point?'''
# Date Created : 14-11-2021 | Date Edited : 14-11-2021

# v**2-u**2=2gs ; g = 9.8 m/s2 --- Formula
# When Object Reaches Max Height, V = 0
# 0-2500 = -19.6s
# s = 127.55
# v = u + gt
# 0 = 50 + (-9.8)t
# t = 5.10

V = 0
U = int(input('\nEnter The Initial Velocity Of The Object: '))
VU = V**2-U**2
Height = VU/-19.6
print(f'\nMax Height Reached By The Object: {Height} Meters.')
print(f'Total Distance Covered: {2*Height} Meters.')

Time = V-U/-9.8
print(f'Total Time Taken By The Object: {Time} Seconds.\n')


