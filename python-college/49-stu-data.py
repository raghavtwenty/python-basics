"""
Q49. student data management, relations and combinations.
                        author @raghav
Date Created : 7 Jan 2022 | Last Updated : 7 Jan 2022
"""


# Functions
def transcript(course_details, student_details, other_data) :

    dummy_tup = [ ]
    for student in student_details :

        for data in other_data :

            for course in course_details :

                if ((student[0] == data[0]) and (data[1] == course[0])) :
                    content = [student, course, data[2]]

                    dummy_tup.append(content)
   
    return dummy_tup 


# Main
print('\nFinding The Student Relationship With Course And Marks.\n')

course_details = [ ("MA101", "Calculus"),
                            ("PH101", "Mechanics"),
                            ("HU101", "English") ]

student_details = [ ("UGM2018001", "Rohit Grewal"),
                             ("UGP2018132", "Neha Talwar") ]

other_data = [ ("UGM2018001", "MA101", "AB"), 
                    ("UGP2018132", "PH101", "B"), 
                    ("UGM2018001", "PH101", "B") ]


returned_tup = transcript(course_details, student_details, other_data)

sorted(returned_tup, key = lambda x : x[2])     # Sort by marks

for i in returned_tup :
    print(i)