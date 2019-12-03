import sys
import os

def main():
    input_file_path = sys.argv[1]

    if not os.path.isfile(input_file_path):
       print(int("File path {} does not exist. Exiting...".format(input_file_path)))
       sys.exit()

    data_raw = open(input_file_path, 'r').readline()
    
    data_string = data_raw.split(",")

    data = list(map(lambda x: int(x), data_string))

    data[1] = 12
    data[2] = 2

    for i in range(0, len(data), 4):
        if i < len(data) - 4:
            slice_data = data[0+i:4+i]
            opcode = slice_data[0]
            pos1 = slice_data[1]
            pos2 = slice_data[2]
            pos_result = slice_data[3]
            if opcode == 1:
                data[pos_result] = data[pos1] + data[pos2]
            elif opcode == 2:
                data[pos_result] = data[pos1] * data[pos2]
            elif opcode == 99:
                break
            else:
                print("Error")
                print("last slice_data : ")
                print(slice_data)
                print("last iteration :")
                print(i)
                sys.exit()

    print(data[0])

if __name__ == '__main__':
    main()