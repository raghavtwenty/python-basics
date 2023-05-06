''' Q5.  Write a program that takes your full name as input and 
displays the abbreviations of the first and middle names 
except the last name which is displayed as it is. 
For example, if your name is Robert Brett Roser, then the output 
should be R.B.Roser.'''

print('\nName Strip.\n')
string = str(input('Enter Your Full Name: '))
strips = string.split()
l = []
for i in strips:
	l.append(i[0])

l.pop(-1)
l.append(strips[-1])

for j in l:
	print(f'{j.capitalize()}.', end ='')
print()
