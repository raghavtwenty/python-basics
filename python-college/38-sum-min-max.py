"""
Q38. Given a list of integers and a value k, print the sum of kth 
maximum element and kth minimum element in the list. 
                        author @raghav
Date Created : 23 Dec 2021 | Last Updated : 23 Dec 2021
"""


# Main
print("\nSum Of Min & Max Number In A List.\n")

lst = str(input("Enter The List Of Numbers: "))
lst = lst.split(",")

mini = 0
maxi = 0
element = int(input("Enter The Kth Element: "))
if str(element) in lst:
    for i in lst:
        i = int(i)
        if i < element:
            mini += i
        elif i > element:
            maxi += i

    print(f"Sum Of Maximum: {maxi}")
    print(f"Sum Of Minimum: {mini}")
else:
    print("Element Not Found.")
