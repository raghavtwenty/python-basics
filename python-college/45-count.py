"""
Q45. Write a program to count the occurrences of each word in given list of words.
Example :
Input List : 'red',' blue', 'green',' white', 'black', 'blue', 'blue', 'red'
Output Format : 
'red': 2, 'blue': 3, 'green': 1, 'white': 1, 'black': 1
                        author @raghav
Date Created : 30 Dec 2021 | 30 Dec 2021
"""


# Main 
print('Counting Occurrences Of Words.\n')

words = str(input("Enter The Words By , (comma): ")).split(',')
set_words = set(words)

for j in set_words :
    wc = words.count(j)
    print(f'{j} : {wc}')

"""
dictionary = dict()
for i in words :    
    if i not in dictionary :    # Appending unique values to the dictionary
        dictionary[i] = 1   # Identified 1st time, so count 1
"""