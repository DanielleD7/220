"""
Name: Danielle Di Pace
hw5.py

Problem: Various functions using and altering strings and lists based on the user's input.

Certification of Authenticity:
I certify that this assignment is entirely my own work.
"""


def name_reverse():
    full_name = input("Enter a name (first last): ")

    space_index = full_name.find(" ")
    first_name = full_name[0:space_index]
    last_name = full_name[space_index + 1:len(full_name)]

    print(last_name + ", " + first_name)


def company_name():
    domain_name = input("Enter a domain: ")

    first_period_index = domain_name.find(".")
    second_period_index = domain_name.rfind(".")
    name_of_company = domain_name[first_period_index + 1:second_period_index]

    print(name_of_company)


def initials():
    number_of_students = eval(input("How many students are in the class? "))

    for i in range(1, number_of_students + 1):
        student_name = input("What is the name of student " + str(i) + "? ")
        student_name = student_name.strip()

        space_index = student_name.find(" ")
        students_initials = student_name[0] + student_name[space_index + 1]
        students_initials = students_initials.strip()

        print(students_initials)


def names():
    full_names = input("Enter a list of first and last names separated by commas: ")
    full_names = full_names.strip()
    names_list = full_names.split(",")
    initial_list = []

    for name in names_list:
        current_name = name.strip()
        space_index = current_name.find(" ")
        name_initials = current_name[0] + current_name[space_index + 1]
        initial_list.append(name_initials)

    print(" ".join(initial_list))


def thirds():
    num_of_sentences = eval(input("Enter the number of sentences: "))
    sentence_list = []

    # Collects the user's sentences and places it into a list
    for i in range(1, num_of_sentences + 1):
        sentence = input("Enter sentence " + str(i) + ": ")
        sentence_list.append(sentence)
    # Sentence Collect for loop END

    # Loops through each sentence in the list
    for sentence in sentence_list:
        index_count = 0
        new_sentence = sentence[index_count]

        # Loops through each character in the sentence if it is divisible by 3
        for _ in range((len(sentence) - 1) // 3):
            index_count = index_count + 3
            new_sentence = new_sentence + sentence[index_count]
        # Character for loop END

        print(new_sentence)
    # Sentence for loop END


def word_average():
    sentence = input("Enter a sentence: ")
    sentence = sentence.strip()
    sentence_list = sentence.split(" ")
    sentence = sentence.replace(" ", "")

    average = len(sentence) / len(sentence_list)
    print("Word Average:", average)


def pig_latin():
    sentence = input("Enter a sentence to convert to pig latin: ")
    sentence_list = sentence.split(" ")
    index = 0

    for word in sentence_list:
        new_word = word[1:len(word)] + word[0] + "ay"
        sentence_list[index] = new_word.lower()
        index = index + 1

    print(" ".join(sentence_list))


if __name__ == '__main__':
    # name_reverse()
    # company_name()
    # initials()
    # names()
    # thirds()
    # word_average()
    # pig_latin()
    pass
