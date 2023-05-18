"""
Q39. Given two lists of integers, l1 and l2, we want to identify those integers from 
each of the lists that are also present in the other list. For instance if l1 is [1,2,4,9,1,2] 
and l2 is [2,3,4,5,4,7,7], we identify [2,4,2] as the numbers from the first list that are 
present in the second list and [2,4,4] as the numbers from the second list that are 
present in the first list. 
                        author @raghav
Date Created : 23 Dec 2021 | Last Updated : 23 Dec 2021
"""


# Functions
def list_dup(lst_1, lst_2):
    dup = [ ]
    for i in lst_1:
        if i in lst_2:
            dup.append(i)
    
    return dup
        

# Main
print("\nFinding Common Elements In Lists.\n")

lst1 = str(input("Enter The Numbers In List 1: "))
lst1 = lst1.split(",")

lst2 = str(input("Enter The Numbers In List 2: "))
lst2 = lst2.split(",")

print(f"Common Elements In List 1: {list_dup(lst1, lst2)}")
print(f"Common Elements In List 2: {list_dup(lst2, lst1)}")
