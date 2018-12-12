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

    # Retrieve an arbitrary MBHEX element in the mesh and extract the tag list.
    root2 = mb2.get_root_set()
    hexes2 = mb2.get_entities_by_type(root2, types.MBHEX)

    if len(hexes2) == 0:
        print("WARNING: No hex elements were found in this data file.")
        exit()

    tag_list2 = mb2.tag_get_tags_on_entity(hexes2[0])

    # Check if each tag is a vector. If so, delete it.
    for tag in tag_list2:
        tag_length = mb2.tag_get_length(tag)
        if tag_length > 1:
            reference_length = tag_length
            tag_name = tag.get_name()
            mb2.tag_delete(tag)

    # Load the mesh file to extract vector tag data from.
    mb1 = core.Core()
    mb1.load_file(mesh_file)

    # Retrieve the MBHEX EntitySet(s) in the mesh.
    root1 = mb1.get_root_set()
    hexes1 = mb1.get_entities_by_type(root1, types.MBHEX)
    tag_list1 = mb1.tag_get_tags_on_entity(hexes1[0])

    # Ensure each vector tag is the same length.
    vector_tags = []
    for tag in tag_list1:
        tag_length = mb1.tag_get_length(tag)
        if tag_length > 1:
            vector_tags.append(tag)
            if mb1.tag_get_length(tag) is not reference_length:
                print("WARNING: Found a vector tag of different length.")
                exit()

    # Make sure the mesh file contains at least one vector tag.
    if len(vector_tags) < 1:
        print("WARNING: This mesh file did not contain any vector tags.")
        exit()

    # Create a directory for the vector tag expansion files.
    input_list = mesh_file.split("/")
    file_name = str(input_list[-1]).split(".")
    dir_name = file_name[0] + "_database"

    # Ensure an existing dictionary is not written over.
    dict_number = 1
    while os.path.isdir(dir_name):
        dir_name = file_name[0] + "_database" + str(dict_number)
        dict_number += 1
    os.mkdir(dir_name)

    """
    For each vector tag, retrieve the scalar value at a specific time state and
    create a scalar tag on the reference mesh. For each time state, write the
    scalar tag values to disk in a vtk file.
    """

    time_state = 0
    while time_state < reference_length:
        scalar_data = []
        for tag in vector_tags:
            data = mb1.tag_get_data(tag, hexes1)
            scalar_data = data[:,time_state]
            data_type = tag.get_data_type()
            scalar_tag = mb2.tag_get_handle("SCALAR_DATA", 1, data_type,
                                            types.MB_TAG_SPARSE, create_if_missing = True)
            mb2.tag_set_data(scalar_tag, hexes2, scalar_data)
        file_location = os.getcwd() + "/" + dir_name + "/" + tag_name + str(time_state) + ".vtk"
        mb2.write_file(file_location)
        time_state += 1

    print(str(time_state) + " files have been written to disk.")


def main():

    # Parse arguments.
    args = parse_arguments()

    # Expand the vector tags from the data file and write each to disk.
    tag_expansion(args.meshfile, args.outputfile, args.tags)


if __name__ == "__main__":
    main()
