''' Q5.
Write a program to print the Floyd's Triangle.
1
01
101
0101
10101'''

print("\nFloyd's Triangle\n") 
rows = int(input("Enter The Total Number Of Rows: "))


for i in range(1, rows+1):
    l2 = ''        
    a = '01'*i
    for k in a: 
        l2+=k  

    len_l2 = int(len(l2)/2)  
    splits = a[len_l2:] 
    print(f'{splits} ')






''' list method
print("\nFloyd's Triangle\n") 
rows = int(input("Enter The Total Number Of Rows: "))

l=[]
for i in range(1, rows+1):
    l2 = []        
    a = '01'*i #01 #0101
    print(a)
    for k in a: #01
        l2.append(k)

    len_l2 = int(len(l2)/2)
    splits = a[len_l2:]


    l.append(splits)

for x in l:
    print(x)

'''
