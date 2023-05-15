""" 
Q2. Find out the maximum length of the possible palindrome
                        author @raghav
Date Created: 10 Dec 2021 | Last Updated : 16 Dec 2021
"""
"""
def findLongest Palindrome (str):

count = [0] *256 for i in range (len (str)):

count [ord (str[i])] += 1

beg=""

mid=""

end =""

ch = ord ('a')

while ch<= ord ('z')

if (count [ch] & 1 ) :

mid = ch

count [ch] -= 1

ch -= 1

else:

for i in range (count //2):

beg chr (ch)

ch +=1

end = beg

end = end [::-1]

return beg + chr (mid) + end

n = int (input())

L=[]

for a in range (n):

L.append (len (findLongest Palindrome (input())))

for b in L:

print (b)

"""
"""
BACKUP _3
# Importing Required Functions
import math

# Funtions
def isPalindrome(*string):

    # Split Check
    match_char = ""
    for i in string:
        reverse = i[::-1]
        for j in range(len(i)):
            if (i[j]==reverse[j]):
                match_char += i[j]
            
    
    # Final Show
    print(match_char)
    print(f"\nThe Maximum Length Of The Possible Palindrome {len(match_char)}")


# Main
print("\nMaximum Length Of The Possible Palindrome.\n")
string  = str(input("Enter The String: ")).lower()
isPalindrome(string)


"""




'''
BACKUP - 1
# Counting Repetitions 
    count_list = [ ]
    for i in lst:
        count  = lst.count(i)
        count_list.append(count)
    
    # Strike Of The Symmetrical Characters
    print(count_list)
    two_count = int((count_list.count(2))/2)
    print(two_count)

    # Checking For Middle Term If Any 
    middle_term_exists = 0
    if 1 in count_list:
        middle_term_exists = 1

    # Use Of Set To Elminate Repetion Of Values


    # Final Show
    max_len = middle_term_exists+two_count
    print(f"\nMaximum Length Of The Possible Palindrome Can Be: {max_len} ")

'''
"""
BACKUP 2

"""
"""for i in string:
        global mid
        length = len(i)
        
        # Finding Mid Value For Odd Terms
        if length%2==1:
            mid = length/2
            mid = math.ceil(mid)
            print(mid)"""

    

    
# A O(n ^ 2) time and O(1) space program to find the
# longest palindromic substring

# This function prints the longest palindrome substring (LPS)
# of str[]. It also returns the length of the longest palindrome

"""
def longestPalSubstr(string):
	maxLength = 1

	start = 0
	length = len(string)

	low = 0
	high = 0

	# One by one consider every character as center point of
	# even and length palindromes
	for i in xrange(1, length):
		# Find the longest even length palindrome with center
		# points as i-1 and i.
		low = i - 1
		high = i
		while low >= 0 and high < length and string[low] == string[high]:
			low -= 1
			high += 1

		# Move back to the last possible valid palindrom substring
		# as that will anyway be the longest from above loop
		low += 1
		high -= 1
		if string[low] == string[high] and high - low + 1 > maxLength:
            start = low
            maxLength = high - low + 1

            # Find the longest odd length palindrome with center
            # point as i
            low = i - 1
            high = i + 1
            while low >= 0 and high < length and string[low] == string[high]:
                low -= 1
                high += 1

            # Move back to the last possible valid palindrom substring
            # as that will anyway be the longest from above loop
            low += 1
            high -= 1
            if string[low] == string[high] and high - low + 1 > maxLength:
            start = low
            maxLength = high - low + 1

        print "Longest palindrome substring is:",
        print string[start:start + maxLength]

        return maxLength


# Driver program to test above functions
string = "forgeeksskeegfor"
print ("Length is: " + str(longestPalSubstr(string)))
"""
def ispalindrome(str, low, high): # geeg ,0 ,3
        for i in range(low, high + 1): # 0,4
                print(str[i], end = "")

def longestPalSubstr(str): #geeg
        n = len(str) #4

        maxLength = 1
        start = 0

        for i in range(n): #0 - 4, 0 
            for j in range(i, n): #0 - 4, 0 , 1, 2, 3
                 flag = 1 # default

                 for k in range(0,((j - i) // 2) + 1):  
                                            #0-0//2+1   = 0 # g g
                                            #1-0//2+1  =0 # g e 
                                            # 2 -0//2+1 = 2 #  g <- e <- e
                                            # 3-0//2 +1 = 2 # 
                         if (str[i + k] != str[j - k]):  # cmp g 2nd e # 2nd iter g & 1st e
                                 flag = 0 # g e 


                 if (flag != 0 and (j - i + 1) > maxLength):
                     #true              0-0+1  # first iteration not vaild
                     #true              3-0+1 # 3rd iter 
                         start = i # 0
                         maxLength = j - i +1    # 0-0+1;  #2

                
        print( "Longest palindrome subString is :",end=" ")
        ispalindrome(str, start, start + maxLength - 1) # geeg ,0 ,3
        return maxLength

# Main 
print("\nMaximum Length Of The Possible Palindrome.\n")
str = input("Enter the string:")
print("\nLength is: ", longestPalSubstr((str))) #geeks