"""
Q41. Return the count values of the circles in characters in a string
                        author @raghav
Date Created : 23 Dec 2021 | Last Updated : 23 Dec 2021
"""


# Main
print("\nReturns The Count Values Of The Circles In Characters In A String.\n")

string = str(input("Enter The String: ")).upper()
print(f"In Terms Of Caps: {string}")
holes_1 = ["A", "D", "O", "P", "Q", "R"]
holes_2 = ["B"]

count = 0
for i in string:
    if i in holes_1:
        count += 1
    elif i in holes_2:
        count += 2
    else:
        count += 0

print(f"Total Count Value: {count}")
if string == "SOORU":
    print("The Word SOORU Has 3 Closed Circles, Most People Eat Three Times A Day.")
