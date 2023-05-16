"""
Q5. Print the length of the joined string and the string itself.
                        author @raghav
Date Created : 10 Dec 2021 | Last Updated : 10 Dec 2021
"""


# Functions
def joining(s1, s2):
    str3 = s1+s2 
    print("\nAfter joining Two Strings.\n")
    print(str3)

    # Counting
    count = 0
    for i in str3:
        count+=1

    print(f"Total Length Of The String: {count}")


# Main
print("\nCounting The Length Of The Two Strings.\n")

str1 = str(input("Enter The First String: "))
str2 = str(input("Enter The Second String: "))
joining(s1=str1, s2=str2)
