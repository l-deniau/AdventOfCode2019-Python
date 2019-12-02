import sys
import os
import math

def main():
    input_file_path = sys.argv[1]

    if not os.path.isfile(input_file_path):
       print("File path {} does not exist. Exiting...".format(input_file_path))
       sys.exit()

    result = 0

    with open(input_file_path, 'r') as input_data:
        for line in input_data:
            result += math.floor(int(line) / 3) - 2
    
    print(result)

if __name__ == '__main__':
    main()