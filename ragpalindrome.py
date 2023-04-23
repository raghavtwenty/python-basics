
def isPalindrome(s):
	return s == s[::-1]

s = str(input('enter the string:'))
ans = isPalindrome(s)

if ans:
	print("it is a palindrome")
else:
	print("it is not a palindrome")

