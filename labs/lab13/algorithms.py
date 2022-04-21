"""
Name: Danielle Di Pace
algorithms.py

Problem: Reads values from a file and place them in a list. A search function that finds returns true or false
if the value passed in was found in the list passed in. A selection sort, a function to calculate the area of
a rectangle, and a sort for rectangles by their area's.

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


def selection_sort(values):
    unsort_index = 0
    small_value_index = unsort_index

    while unsort_index < len(values):
        small_value = values[unsort_index]

        # Finds the smallest value in the unsorted part of the list
        for index in range(unsort_index, len(values)):
            if small_value > values[index]:
                small_value = values[index]
                small_value_index = index
        # for loop END

        # Swap values with the first index of the unsorted part of the list
        if small_value < values[unsort_index]:
            values[unsort_index], values[small_value_index] = values[small_value_index], values[unsort_index]

        unsort_index += 1
    # while loop END


def calc_area(rect):
    length = abs(rect.getP1().getX() - rect.getP2().getX())
    height = abs(rect.getP1().getY() - rect.getP2().getY())

    return length * height


def rect_sort(rectangles):
    unsort_index = 0
    small_rect_index = unsort_index

    while unsort_index < len(rectangles):
        small_rect = rectangles[unsort_index]
        small_area = calc_area(small_rect)

        # Finds the rectangle with the smallest area in the list
        for index in range(unsort_index, len(rectangles)):
            if small_area > calc_area(rectangles[index]):
                small_rect = rectangles[index]
                small_area = calc_area(small_rect)
                small_rect_index = index
        # for loop END

        # Swap the values with the first index of the unsorted part of the list
        if small_area < calc_area(rectangles[unsort_index]):
            rectangles[unsort_index], rectangles[small_rect_index] \
                = rectangles[small_rect_index], rectangles[unsort_index]

        unsort_index += 1
    # while loop END
