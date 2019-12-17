from anytree import Node, RenderTree, AsciiStyle, Walker

import sys
import os
import types

def main():
    input_file_path = sys.argv[1]

    if not os.path.isfile(input_file_path):
       print(int("File path {} does not exist. Exiting...".format(input_file_path)))
       sys.exit()

    input_data = open(input_file_path, 'r').read().splitlines()

    node_list = {}

    for data in input_data:
        space_object_data = data.split(")")
        mass_object = Node(space_object_data[0])
        orbit_object = Node(space_object_data[1])

        if mass_object.name in node_list:
            mass_object = node_list[mass_object.name]
        else:
            node_list[mass_object.name] = mass_object

        if orbit_object.name in node_list:
            orbit_object = node_list[orbit_object.name]
        else:
            node_list[orbit_object.name] = orbit_object

        orbit_object.parent = mass_object

    w = Walker()
    walk_path = w.walk(node_list["YOU"].parent, node_list["SAN"].parent)
    print(len(flatten(walk_path))-1)


def flatten(T):
    if type(T) != tuple: return (T,)
    elif len(T) == 0: return ()
    else: return flatten(T[0]) + flatten(T[1:])


if __name__ == '__main__':
    main()