import sys
import os

def main():
    input_file_path = sys.argv[1]

    if not os.path.isfile(input_file_path):
       print(int("File path {} does not exist. Exiting...".format(input_file_path)))
       sys.exit()
    
    try:
        input_value = int(sys.argv[2])
    except ValueError:
        print("Input id expected {} is not a number. Exiting...".format(sys.argv[2]))
        sys.exit()
    except IndexError:
        print("Input id is missing ! Exiting...")
        sys.exit()

    data_raw = open(input_file_path, 'r').readline()
    data_string = data_raw.split(",")
    data = [int(char) for char in data_string]

    output_values = []

    i = 0
    while i < len(data):
        first_int = data[i]
        opcode = first_int % 100
        first_param_mode = int(first_int/100%10)
        second_param_mode = int(first_int/1000%10)
        # third_param_mode = int(first_int/10000%10)
        if opcode == 1:
            first_param = data[i+1] if first_param_mode else data[data[i+1]]
            second_param = data[i+2] if second_param_mode else data[data[i+2]]
            data[data[i+3]] = first_param + second_param
            i += 4
        elif opcode == 2:
            first_param = data[i+1] if first_param_mode else data[data[i+1]]
            second_param = data[i+2] if second_param_mode else data[data[i+2]]
            data[data[i+3]] = first_param * second_param
            i += 4
        elif opcode == 3:
            data[data[i+1]] = input_value
            i += 2
        elif opcode == 4:
            output_values.append(data[data[i+1]])
            i += 2
        elif opcode == 5:
            first_param = data[i+1] if first_param_mode else data[data[i+1]]
            second_param = data[i+2] if second_param_mode else data[data[i+2]]
            if first_param: i = second_param
            else: i += 3
        elif opcode == 6:
            first_param = data[i+1] if first_param_mode else data[data[i+1]]
            second_param = data[i+2] if second_param_mode else data[data[i+2]]
            if not first_param: i = second_param
            else: i += 3
        elif opcode == 7:
            first_param = data[i+1] if first_param_mode else data[data[i+1]]
            second_param = data[i+2] if second_param_mode else data[data[i+2]]
            data[data[i+3]] = 1 if first_param < second_param else 0
            i += 4
        elif opcode == 8:
            first_param = data[i+1] if first_param_mode else data[data[i+1]]
            second_param = data[i+2] if second_param_mode else data[data[i+2]]
            data[data[i+3]] = 1 if first_param == second_param else 0
            i += 4
        elif opcode == 99:
            break
        else:
            print("Error")
            print("last iteration :")
            print(i)
            print("opcode :")
            print(opcode)
            sys.exit()


    print(output_values)


if __name__ == '__main__':
    main()