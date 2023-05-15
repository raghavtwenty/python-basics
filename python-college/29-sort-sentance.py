"""
Q1. Sort the entered words in alphabetical order
                        author @raghav
Date Created : 10 Dec 2021 | Last Updated : 11 Dec 2021
"""


# function
def sort_fun (split, length):
    print("\nWords In Alphabetical Order As Follows...")
    for i in range(length-1): 
        for j in range(length-i-1): 
            if split[j]>=split[j+1]:
                split[j], split[j+1] = split[j+1],split[j] 
    
    print(split)


# Main
print("\nSorting Words In Alphabetical Order.\n")
sent = str(input("Enter Comma Separated Words: "))
split =  sent.split(",")
length = len(split)
sort_fun(split, length)




"""
Character Sorting
s= ["c","h","a","A","a","q","0","9"," "]
y=[]
count=0
while len(y)< len(s):
    for i in s:
        if ord(i)==count:
            y.append(i)
    count+=1
print (y)
"""