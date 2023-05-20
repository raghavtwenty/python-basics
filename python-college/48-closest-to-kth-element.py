"""
Q48. Write a program to find the closest pair to Kth index element in Tuple. 
                        author @raghav
Date Created : 30 Dec 2021 | Last Updated : 8 Jan 2022
"""


# Main
print('\nFinding The Nearest Pair.\n')

#test_list = [(3, 4), (78, 76), (2, 3), (9, 8), (19, 23)]
test_list =  [(3, 4, 9), (5, 6, 7)]
print(f'List : {test_list}')

#tup = (17, 23)
tup = (1, 2, 5)
print(f'Closest Element To Be Found: {tup}')

#k = 2
k = 3
print(f'Nearest Index : {k}')
k = k - 1       # Reduce as index starts from 0

test_list.append(tup)       # Append the tuple to the original list
test_list = sorted(test_list, key = lambda tup : tup[k])       # After Appending sort the list
# Sort by k th element of the tuple, use of key and lambda 
print(test_list)

if (test_list.index(tup) == -1) :
    '''If the tup element is the last item in the sorted list, 
    then the only nearest element is the last minus -1, that has the index -2
    '''
    print(test_list[-2])

elif (test_list.index(tup) == 0) :
    '''If the tup element is the first item in the sorted list, 
    then the only nearest element is the first element, that has the index 1
    '''
    print(test_list[1])

else :      # If the tup element is neither first nor last in the sorted list

    index_tup = test_list.index(tup)        # Find the index of the tup element in the sorted list

    next_index_tup = index_tup + 1      # Index of the next element - ref. tup
    previous_index_tup = index_tup - 1      # Index of the previous element - ref. tup

    next_diff = test_list[next_index_tup][k] - test_list[index_tup][k]  
    # Compare the differences of the k th element in the tuple (next index value)
    previous_diff = test_list[index_tup][k] - test_list[previous_index_tup][k]
    # Compare the differences of the k th element in the tuple (previous index value)

    # Figure out the least differences
    if next_diff <= previous_diff :
        print(f'Closest Element : {test_list[index_tup+1]}')       # Final show
    else :
        print(f'Closest Element : {test_list[index_tup-1]}')       # Final show

