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
    same_adjacent_digits = False
    digit_list = [int(char) for char in str(number)]
    for i in range(0, len(digit_list) - 1, 1):
        if digit_list[i] == digit_list[i+1]:
            same_adjacent_digits = True
        elif digit_list[i] > digit_list[i+1]:
            return False
    return same_adjacent_digits


if __name__ == '__main__':
    main()