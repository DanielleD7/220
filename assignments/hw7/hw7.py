"""
Name: Danielle Di Pace
hw7.py

Problem: Reading and writing to files, altering their contents and encoding
messages with an imported encryption file

Certification of Authenticity:
I certify that this assignment is entirely my own work.
"""
from encryption import encode, encode_better


def number_words(in_file_name, out_file_name):
    words_file = open(in_file_name, "r")
    numbered_words = open(out_file_name, "w")

    words = words_file.read()
    words = words.replace("\n", " ")
    words = words.strip()
    words = words.split(" ")

    count = 1
    for word in words:
        print(str(count) + " " + word, file=numbered_words)
        count = count + 1

    words_file.close()
    numbered_words.close()


def hourly_wages(in_file_name, out_file_name):
    employee_wages = open(in_file_name, "r")
    employee_week_pay = open(out_file_name, "w")
    bonus_rate = 1.65

    for line in employee_wages.readlines():
        employee_info = line.strip().replace("\n", " ").split(" ")

        wage = float(employee_info[2]) * float(employee_info[3])
        wage = wage + (float(employee_info[3]) * bonus_rate)

        print(employee_info[0] + " " + employee_info[1] + " {:.2f}".format(wage), file=employee_week_pay)

    employee_wages.close()
    employee_week_pay.close()


def calc_check_sum(isbn):
    isbn = isbn.strip().replace("-", "")

    check_sum = 0
    count = len(isbn)
    for number in isbn:
        check_sum = check_sum + (int(number) * count)
        count = count - 1

    return check_sum


def send_message(file_name, friend_name):
    message_file = open(file_name, "r")
    friend_message = open(friend_name + ".txt", "w")

    print(message_file.read(), end="", file=friend_message)

    message_file.close()
    friend_message.close()


def send_safe_message(file_name, friend_name, key):
    message_file = open(file_name, "r")
    safe_message_file = open(friend_name + ".txt", "w")

    for line in message_file.readlines():
        code = encode(line.replace("\n", ""), key)
        print(code, file=safe_message_file)


def send_uncrackable_message(file_name, friend_name, pad_file_name):
    message_file = open(file_name, "r")
    pad_file = open(pad_file_name, "r")
    uncrackable_message = open(friend_name + ".txt", "w")

    code = encode_better(message_file.read(), pad_file.read())
    print(code, file=uncrackable_message)

    message_file.close()
    pad_file.close()
    uncrackable_message.close()


if __name__ == '__main__':
    pass
