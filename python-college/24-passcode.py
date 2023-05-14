''' Q4.
Write a Python program to check the validity of a password given 
by the user.
1. Contain at least 1 letter between a and z
2. Contain at least 1 number between 0 and 9
3. Contain at least 1 letter between A and Z
4. Contain at least 1 character from $, #, @
5. Minimum length of password: 6
6. Maximum length of password: 12 '''

print('\nPasscode Validator.\n')

string = str(input('Enter The Passcode To Validate: '))

alpha_s = False
alpha_u = False
Num = False
spl_c = False

if len(string)>=6 and len(string)<=12:
	for i in string:
		if i.isupper():
			alpha_u = True
		elif i.islower():
			alpha_s = True
		elif i.isdigit():
			Num = True
		else:
			spl_c = True
	
else:
	print('\nPasscode Length Less Than 6 Character Or Exceeds 12 Character.')


if alpha_s == False:
	print('\nLowercase Character Missing.')
elif alpha_u == False:
	print('\nUppercase Character Missing.')
elif Num == False:
	print('\nNumber Missing.')
elif spl_c == False:
	print('\nSpecial Character Missing.')
else: 
	print('\nPerfect!!!')