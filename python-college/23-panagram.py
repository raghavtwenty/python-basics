''' Q3. 
A panagram is a sentence containing every 26 letters in the English 
alphabet. Given a string S, check if it is panagram or not.

Input Format:
The first line contains the sentence S. 
Output Format:
Print 'YES' or 'NO' accordingly 

Example: 
Input: The quick brown fox jumps over the lazy dog 
Output: YES
'''

total_str = {' ','A','B','C','D','E','F','G','H','I','J','K',
'L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z'}

print('\nPangram Or Not.\n')

string = str(input('Enter The String: ')).upper()
sett = set()
for i in string:
    sett.add(i)

if len(total_str.difference(sett)) == 0:
    print('YES')
else:
    print('NO')
