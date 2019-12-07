#!/usr/bin/env python3

# Created by: Andrei Chirilov
# Created on: November 2019
# This program get's a list of numbers and finds the largest number

import random


def calculate(array_of_numbers):
    # This function finds the largest number from random list

    # Variables
    largest_array_num = 0

    # Process
    for repeater in range(len(array_of_numbers)):
        if array_of_numbers[repeater] > largest_array_num:
            largest_array_num = array_of_numbers[repeater]

    # Output
    return largest_array_num


def main():
    # This function creates an array and shows the numbers

    # Array
    number_array = []

    # Adding numbers to an array
    for repeater in range(0, 9):
        random_number = random.randint(1, 100)
        print("Random Number " + str(repeater + 1) + " is: " +
              str(random_number))
        number_array.append(random_number)

    # Process
    largest_number = calculate(number_array)

    # Output
    print("The largest number is: ", largest_number)


if __name__ == "__main__":
    main()
