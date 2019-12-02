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
            result += get_fuel_required(int(line), 0)
    
    print(result)

def get_fuel_required(mass, total):
    if mass < 9:
        return total
    else:
        fuel_required = math.floor(mass / 3) - 2
        total += fuel_required
        return get_fuel_required(fuel_required, total)

if __name__ == '__main__':
    main()