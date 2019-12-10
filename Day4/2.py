import sys
import os
import time

def main():

    start = time.time()

    input_puzzle = sys.argv[1]

    min_input = int(input_puzzle.split("-")[0])
    max_input = int(input_puzzle.split("-")[1])

    match_counter = 0

    for number in range(min_input, max_input, 1):
        if check_number(number):
            match_counter += 1

    print(match_counter)

    end = time.time()
    execution_duration = (end - start) % 60
    print("Executed in : " + str(execution_duration) + " seconds")


def check_number(number):
    same_adjacent_2_digits = False
    digit_list = [int(char) for char in str(number)]
    i = 0
    while i < len(digit_list) - 1:
        if digit_list[i] == digit_list[i+1]:
            same_digit = digit_list[i]
            next_occurence = get_next_occurence(same_digit, digit_list[i+2:])
            if next_occurence == 0:
                same_adjacent_2_digits = True
                i += 1
            else:
                i += (1 + next_occurence)
        elif digit_list[i] > digit_list[i+1]:
            return False
        else:
            i += 1
    return same_adjacent_2_digits


def get_next_occurence(same_digit, digit_list):
    occurence = 0
    for digit in digit_list:
        if digit != same_digit:
            return occurence
        else:
            occurence += 1
    return occurence


if __name__ == '__main__':
    main()