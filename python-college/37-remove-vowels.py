"""
Q37. Given a string s, remove all the vowels in s and reprint the string. 
The order of other characters in the string should be maintained. 
                        author @raghav
Date Created : 23 Dec 2021 | Last Updated : 23 Dec 2021
"""


# Main
print("\nRemove The Vowels In The String.\n")

str1 = str(input("Enter The String: ")).lower()
str1 = list(str1)
for i in str1:
    if (i not in ("a", "e", "i", "o", "u")):
        print(f"{i}", end="")
