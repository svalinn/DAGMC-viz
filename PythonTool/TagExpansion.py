import argparse
import os
from pymoab import core, tag, types


def parse_arguments():
    """
    Parse the argument list and return a mesh file location, an optional output
    file name, and an optional list of specific tag names to expand.

    Input:
    ______
       none

    Returns:
    ________
       args: Namespace
           User supplied mesh file location, optional output file name, and
           optional list of tag names.
    """

    parser = argparse.ArgumentParser(description="Expand vector tags to scalar tags.")

    parser.add_argument("meshfile",
                        type=str,
                        help="Provide a path to the mesh file."
                        )
    parser.add_argument("-o", "--outputfile",
                        type=str,
                        help="Provide a base name for the output file(s)."
                        )
    parser.add_argument("-t", "--tags",
                        type=list,
                        help="Only expand the tags with these name values."
                        )

    args = parser.parse_args()

    return args


def tag_expansion(mesh_file, output_file = None, tag_list = None):
    """
    Expand the vector tags in the given mesh data file. Write a file to disk
    for each time state with the corresponding scalar tag values from each vector tag.

    Input:
    ______
       mesh_file: str
           User supplied mesh file location.
       output_file: str
           Optional user supplied output file name.
       tag_list: Array
           Optional user supplied array of tag name values.

    Returns:
    ________
       none
    """

    # Load the mesh file to create a reference mesh.
    mb2 = core.Core()
    mb2.load_file(mesh_file)

    # Retrieve the MBHEX EntitySet(s) in the mesh.
    root = mb2.get_root_set()
    hexes = mb2.get_entities_by_type(root, types.MBHEX)

    if len(hexes) == 0:
        print("WARNING: No hex elements were found in this data file.")
        exit()

    # Retrieve an arbitrary MBHEX element and extract the tag list.
    tag_list = mb2.tag_get_tags_on_entity(hexes[0])

    # Check if each tag is a vector. If so, delete it.
    for tag in tag_list:
        tag_length = mb2.tag_get_length(tag)
        if tag_length > 1:
            reference_length = tag_length
            mb2.tag_delete(tag)

    # Load the mesh file.
    mb1 = core.Core()
    mb1.load_file(mesh_file)

    # Retrieve the MBHEX EntitySet(s) in the mesh.
    root = mb1.get_root_set()
    hexes = mb1.get_entities_by_type(root, types.MBHEX)
    tag_list = mb1.tag_get_tags_on_entity(hexes[0])

    # Ensure each vector tag is the same length.
    vector_tags = []
    for tag in tag_list:
        tag_length = mb1.tag_get_length(tag)
        if tag_length > 1:
            vector_tags.append(tag)
            if mb1.tag_get_length(tag) is not reference_length:
                print("WARNING: Found vector tag of different length.")
                exit()

    time_state = 0
    while time_state < reference_length:
        scalar_data = []
        for tag in vector_tags:
            data = mb1.tag_get_data(tag, hexes)
            scalar_data.append(data[:,time_state])
            data_type = tag.get_data_type()
        scalar_tag = mb2.tag_get_handle("SCALAR_DATA", 1, data_type,
                                        types.MB_TAG_SPARSE, create_if_missing=True)
        mb2.tag_set_data(scalar_tag, hexes, scalar_data)
        mb2.write_file("time_state_" + time_state + ".vtk")
        time_state += 1

    # TODO: Fix AssertionError during scalar tag creation.
    # TODO: Write separate function to return tag list on user specified element.

    """
    OLD CODE

    # Load the mesh file for operation.
    mb1 = core.Core()
    mb1.load_file(mesh_file)

    # Retrieve the MBHEX EntitySet(s) in the mesh.
    root = mb.get_root_set()
    hexes = mb.get_entities_by_type(root, types.MBHEX)

    if len(hexes) == 0:
        print("WARNING: No hex elements were found in this data file.")
        exit()

    # Retrieve an arbitrary MBHEX element and extract the tag list.
    tag_list = mb.tag_get_tags_on_entity(hexes[0])

    # Create a directory for the expanded vector tag files.
    input_list = mesh_file.split("/")
    file_name = str(input_list[-1]).split(".")
    dir_name = file_name[0] + "_expanded_tags"
    i = 0
    while os.path.isdir(dir_name):
        dir_name = file_name[0] + "_expanded_tags_" + str(i)
        i += 1
    os.mkdir(dir_name)

    # Check if each tag is a vector or a scalar.
    for tag in tag_list:
        tag_length = mb.tag_get_length(tag)

        # If it is a vector, expand and write to disk.
        if tag_length > 1:
            data = mb.tag_get_data(tag, hexes)
            i = 0
            for vector in data:

                # Determine if the user supplied an output file name.
                if output_file:
                    base_file_name = output_file + "_"
                else:
                    base_file_name = tag.get_name()

                # Write a file with the scalar values from each vector tag expansion.
                file = open(base_file_name + str(i) + ".vtk","w")
                j = 0
                while j < len(vector):
                    scal_tag_j = vector[j]
                    file.write(str(scal_tag_j) + "\n")
                    j +=1
                i += 1

    print(str(len(data)) + " vector tags have been expanded and written to disk.")
    """


def main():

    # Parse arguments.
    args = parse_arguments()

    # Expand the vector tags from the data file and write each to disk.
    tag_expansion(args.meshfile, args.outputfile, args.tags)


if __name__ == "__main__":
    main()
