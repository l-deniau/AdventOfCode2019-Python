import sys
import os

def main():
    input_file_path = sys.argv[1]

    if not os.path.isfile(input_file_path):
       print(int("File path {} does not exist. Exiting...".format(input_file_path)))
       sys.exit()

    data_raw = open(input_file_path, 'r').readline()
    digits = [int(char) for char in data_raw]

    WIDE = 25
    TALL = 6
    TOTAL_DIGIT_LAYER = WIDE * TALL

    layer_list = [digits[x:x+TOTAL_DIGIT_LAYER] for x in range(0,len(digits),TOTAL_DIGIT_LAYER)]

    fewer_0_digit_layer = min(layer_list, key=(lambda layer: layer.count(0)))

    print(fewer_0_digit_layer.count(1)*fewer_0_digit_layer.count(2))


if __name__ == '__main__':
    main()