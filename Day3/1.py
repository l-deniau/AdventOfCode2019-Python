import sys
import os
import time

def main():

    start = time.time()

    input_file_path = sys.argv[1]

    if not os.path.isfile(input_file_path):
       print(int("File path {} does not exist. Exiting...".format(input_file_path)))
       sys.exit()

    data_raw = open(input_file_path, 'r').readlines()

    first_wire_path = data_raw[0]
    second_wire_path = data_raw[1]

    vertical_lines = {}
    horizontal_lines = {}
    intersect_list = []

    current_position = [0,0]

    for direction in first_wire_path.split(","):
        line = process_wire_direction(direction, current_position)
        if line[2] == "v":
            vertical_lines.setdefault(current_position[0], [(line[0],line[1])]).append((line[0],line[1]))
        elif line[2] == "h":
            horizontal_lines.setdefault(current_position[1], [(line[0],line[1])]).append((line[0],line[1]))
        
    current_position = [0,0]

    for direction in second_wire_path.split(","):
        line = process_wire_direction(direction, current_position)
        intersects_of_line = get_intersect(line, current_position, vertical_lines, horizontal_lines)
        intersect_list.extend(intersects_of_line)

    min_manhattan_distance_point = min(intersect_list, key=get_manhattan_distance)

    print(get_manhattan_distance(min_manhattan_distance_point))

    end = time.time()
    execution_duration = (end - start) % 60
    print("Executed in : " + str(execution_duration) + " seconds")


def process_wire_direction(direction, current_position):
    if direction.startswith("U"):
        initial_y = current_position[1]
        current_position[1] += int(direction[1:])
        return (initial_y,current_position[1],"v")
    elif direction.startswith("D"):
        initial_y = current_position[1]
        current_position[1] -= int(direction[1:])
        return (current_position[1],initial_y,"v")
    elif direction.startswith("R"):
        initial_x = current_position[0]
        current_position[0] += int(direction[1:])
        return (initial_x, current_position[0],"h")
    elif direction.startswith("L"):
        initial_x = current_position[0]
        current_position[0] -= int(direction[1:])
        return (current_position[0],initial_x,"h")
    else:
        print("ERROR")
        print(direction)


def get_intersect(line, current_position, vertical_lines, horizontal_lines):
    intersects_of_line = []
    if line[2] == "h":
        for x in range(line[0], line[1], 1):
            if x in vertical_lines:
                for x_line in vertical_lines[x]:
                    if x_line[0] <= current_position[1] <= x_line[1]:
                        intersects_of_line.append((x, current_position[1]))
    elif line[2] == "v":
        for y in range(line[0], line[1], 1):
            if y in horizontal_lines:
                for y_line in horizontal_lines[y]:
                    if y_line[0] <= current_position[0] <= y_line[1]:
                        intersects_of_line.append((current_position[0], y))
    return intersects_of_line


def get_manhattan_distance(intersect):
    return abs(intersect[0]) + abs(intersect[1])


if __name__ == '__main__':
    main()