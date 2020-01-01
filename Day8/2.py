import sys
import os
import pprint

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

    layer_pixel = {}
    result = []
    counter = 0

    for digit in digits:
        counter = counter % TOTAL_DIGIT_LAYER
        layer_pixel.setdefault(counter, []).append(digit)
        counter += 1

    for pixel_list in layer_pixel.values():
        result.append(decode_pixel(pixel_list))

    pp = pprint.PrettyPrinter()
    pp.pprint([result[x:x+WIDE] for x in range(0, len(result), WIDE)])


def decode_pixel(pixel_list):
    for pixel in pixel_list:
        if pixel == 0 or pixel == 1:
            return pixel
    return 2


if __name__ == '__main__':
    main()