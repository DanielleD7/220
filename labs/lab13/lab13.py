"""
Name: Danielle Di Pace
lab13.py

Problem: Searches through a file of signal values to find a neutron star and displays the results.

Certification of Authenticity:
I certify that this assignment is entirely my own work.
"""
from algorithms import *
from graphics import *


def star_find(filename):
    signal_file = open(filename, "r")
    signal_count = 0
    signal_list = signal_file.read().split(" ")
    strong_signal_list = []

    for signal in signal_list:
        signal_count += 1
        if 4000 <= eval(signal) <= 5000:
            strong_signal_list.append(signal)
        if len(strong_signal_list) == 5:
            break
    # for loop END

    print("Number of Strong Signals:", len(strong_signal_list))
    print("Strong Signals Found: ", end="")
    for signal in strong_signal_list:
        print(signal, end=" ")

    if len(strong_signal_list) == 5:
        print("\nSignals Searched:", signal_count)

    signal_file.close()
