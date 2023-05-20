"""
Q50. Given an array of n string containing lowercase letters. Find the size of largest 
subset of string which are anagram of each others. An anagram of a string is another 
string that contains same characters, only the order of characters can be different. 
For example, “abcd” and “dabc” are anagram of each other.
                        author @raghav
Date Created : 30 Dec 2021 | Last Updated : 8 Jan 2022
"""


# Main
print('\nFinding Anagram.\n')

string = 'ant magenta magnate tan gnamate'.split()
#string = 'cars bikes arcs steer'.split()
print(string)

set_string = [ ]
for set_str in string :         # Make a set of all items in the string
    set_string.append(set(set_str))         # after converting it into set add to the set string list

sorted_by_length = sorted(string, reverse = True, key = len)        # Sort by max length

for item in sorted_by_length :      # Sorted max len list iteration  
    count = 0           # Initialize count to zero

    for i in set_string :           # Iterate contents in the converted set string list
        if set(item) == i :         # Check if each element in the set string list is equal to the ith iterator
            count += 1

    if (count > 1) :       # If the count is > 1 stop, else check for next max anagram
        print(int(count))        # Final show
        break

if (count == 0) :
    print('No Max Anagram Found.')



'''

#str1=input("enter the string:")
str1 = 'ant magenta magnate tan gnamate'
list1=str1.split()
set1=set()
count=0
for i in list1:
    ii = set(i)
    print(ii)
    for j in list1:
        jj = set(j)
        print(ii)
        if ii == jj and list1.index(i) != list1.index(j):
            print(ii , jj ,list1.index(i),list1.index(j))
            count += 1

print(count)

'''