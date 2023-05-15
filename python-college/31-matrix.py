"""
Q3. Rotate the outer elements of the matrix
                        author @raghav
Date Created : 10 Dec 2021 | Last Updated : 16 Dec 2021
"""




"""
# Functions
def rotateMat(mat):
 
    if not len(mat):
        return
     
    '''
        top : starting row index
        bottom : ending row index
        left : starting column index
        right : ending column index
    '''
 
    top = 0
    bottom = len(mat)-1
 
    left = 0
    right = len(mat[0])-1
 
    while left < right and top < bottom:
 
    
        prev = mat[top+1][left]
 
        
        for i in range(left, right+1):
            curr = mat[top][i]
            mat[top][i] = prev
            prev = curr
 
        top += 1
 
        # Move elements of rightmost column one step downwards
        for i in range(top, bottom+1):
            curr = mat[i][right]
            mat[i][right] = prev
            prev = curr
 
        right -= 1
 
        # Move elements of bottom row one step left
        for i in range(right, left-1, -1):
            curr = mat[bottom][i]
            mat[bottom][i] = prev
            prev = curr
 
        bottom -= 1
 
        # Move elements of leftmost column one step upwards
        for i in range(bottom, top-1, -1):
            curr = mat[i][left]
            mat[i][left] = prev
            prev = curr
 
        left += 1
 
    return mat
 

def printMatrix(mat):
    for row in mat:
        print (row)
 


 # Main
print("\nRotating The Outer Elements Of The Matrix.\n")

side_num = int(input("Enter The Number Of Sides: "))


# Matrix Creation
matrix = [ ]

# Matrix Input
for i in range(side_num):
    dummy_matrix = [ ]
    for j in range(side_num):
        element = int(input(f"Enter The Value For The {i+1}th Row and {j+1}th Column: "))
        dummy_matrix.append(element)
    matrix.append(dummy_matrix)

print("\nOriginal Matrix.\n")
for i in matrix:
    print(i)


print("\nMatrix After Rotation\n")
matrix = rotateMat(matrix)
# Print
printMatrix(matrix)


  
"""


"""
#BACKUP

mat_1= [11, 22, 33, 44, 55, 66, 77, 88, 99, 23 ,33 , 43, 53, 63, 73, 83]
print("\nOrignial Matrix")

def matrix(mat):
    count = 1
    multi = side_num

    for i in range(side_num):
        cmf = multi*count
        con_print = mat[:cmf]

        if len(con_print) == side_num:
            print(con_print)
        elif len(con_print) > side_num:
            print(con_print[-side_num:])
        count +=1
        
matrix(mat_1)

print("\nAfter Rotation")
mat_1.insert(0, mat_1[-1])
mat_1.pop()

matrix(mat_1)
# Display Original Matrix
print("\nOriginal Matrix.\n")
for j in matrix:
    print(j)
"""



