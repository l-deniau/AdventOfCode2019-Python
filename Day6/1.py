from anytree import Node, RenderTree

import sys
import os

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

    print(sum([node.depth for node_name, node in node_list.items()]))


if __name__ == '__main__':
    main()