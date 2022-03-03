"""
Name: Danielle Di Pace
lab7.py

Problem: Using the contents of a file to calculate the class average, each student's grade and if they meet
the weight requirement. The results will be outputted to a file.

Certification of Authenticity:
I certify that this assignment is entirely my own work.
"""


def weighted_average(in_file_name, out_file_name):
    grades_file = open(in_file_name, "r")
    avg_file = open(out_file_name, "w")
    grades_list = grades_file.readlines()

    class_average = 0
    class_average_count = 0

    # Loops through each student with their grades in the list
    for file_line in grades_list:
        student_info = file_line.strip()
        colon_index = student_info.find(":")

        student_name = student_info[0:colon_index]
        # Gets a string of the students grades
        student_grades = student_info[colon_index + 2:len(student_info)]
        # Splits the string into a list of grades by " "
        student_grades = student_grades.split(" ")

        student_average = 0
        index = -1
        count = 1
        weight_total = 0
        # Calculates part of the student's average using weights and grades
        for _ in range(len(student_grades) // 2):
            # Weight and Grade format w1 g1 w2 g2 ... wn gn
            new_index = index + count
            student_average = student_average + (eval(student_grades[new_index]) * eval(student_grades[new_index + 1]))
            weight_total = weight_total + eval(student_grades[new_index])

            count = count + 1
            index = index + 1

            #       index   count
            # 0 1    -1      + 1   + 1
            # 2 3     0      + 2   + 1
            # 4 5     1      + 3   + 1
        # Student's Average Calculation Loop END

        student_average = student_average / 100
        avg_file.write(student_name + "'s average: ")  # File

        # Testing for students with the right weight
        if weight_total < 100:
            avg_file.write("Error: The weights are less than 100.\n")  # File
        elif weight_total > 100:
            avg_file.write("Error: The weights are more than 100.\n")  # File
        else:
            avg_file.write(str(student_average) + "\n")  # File

            class_average = class_average + student_average
            class_average_count = class_average_count + 1
    # Individual Students Loop END

    class_average = class_average / class_average_count
    avg_file.write("Class average: " + str(class_average))  # File

    grades_file.close()
    avg_file.close()


weighted_average("grades.txt", "avg.txt")
