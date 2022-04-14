"""
Name: Danielle Di Pace
algorithms.py

Problem: Reads values from a file and place them in a list. A search function that finds returns true or false
if the value passed in was found in the list passed in.

Certification of Authenticity:
I certify that this assignment is entirely my own work.
"""


def read_data(file_name):
    file_list = []
    file = open(file_name, "r")
    line = file.readline()

    while line:
        line = line.replace("\n", "")
        line = line.split(" ")
        while line:
            file_list.append(eval(line.pop(0)))
        line = file.readline()
        # nested while loop END
    # while loop END
    file.close()
    return file_list


def is_in_linear(search_val, values):
    count = 0
    while count < len(values):
        if search_val == values[count]:
            return True
        count += 1
    return False

