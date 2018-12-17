import argparse
import numpy as np
import os
from pymoab import core, tag, types


def parse_arguments():
    """
    Parse the argument list and return a mesh file location.

    Input:
    ______
       none

    Returns:
    ________
       args: Namespace
           User supplied mesh file location.
    """

    parser = argparse.ArgumentParser(description="Expand vector tags to scalar tags.")

    parser.add_argument("meshfile",
                        type=str,
                        help="Provide a path to the mesh file."
                        )

    args = parser.parse_args()

    return args


def tag_expansion(mesh_file):
    """
    Expand the vector tags in the given mesh data file. Write a file to disk
    for each time state with the corresponding scalar tag values from each vector tag.

    Input:
    ______
       mesh_file: str
           User supplied mesh file location.

    Returns:
    ________
       none
    """

    # Load the mesh file to create a reference mesh.
    mb_ref = core.Core()
    mb_ref.load_file(mesh_file)

    # Retrieve an arbitrary MBHEX element in the mesh and extract the tag list.
    root_ref = mb_ref.get_root_set()
    hexes_ref = mb_ref.get_entities_by_type(root_ref, types.MBHEX)

    if len(hexes_ref) == 0:
        print("WARNING: No hex elements were found in this data file.")
        exit()

    tag_list_ref = mb_ref.tag_get_tags_on_entity(hexes_ref[0])

    # Check if each tag is a vector. If so, delete it.
    for tag in tag_list_ref:
        tag_length = mb_ref.tag_get_length(tag)
        if tag_length > 1:
            # Grab the length and name of the vector tag for later use.
            reference_length = tag_length
            tag_name = tag.get_name()
            mb_ref.tag_delete(tag)

    # Load the mesh file for extracting vector tag data.
    mb_ext = core.Core()
    mb_ext.load_file(mesh_file)

    # Retrieve an arbitrary MBHEX element in the mesh and extract the tag list.
    root_ext = mb_ext.get_root_set()
    hexes_ext = mb_ext.get_entities_by_type(root_ext, types.MBHEX)
    tag_list_ext = mb_ext.tag_get_tags_on_entity(hexes_ext[0])

    # Ensure each vector tag is the same length.
    vector_tags = []
    for tag in tag_list_ext:
        tag_length = mb_ext.tag_get_length(tag)
        if tag_length > 1:
            vector_tags.append(tag)
            if mb_ext.tag_get_length(tag) is not reference_length:
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
    For each vector tag, retrieve the scalar value at a specific index and
    create a scalar tag on the reference mesh. For each time state, write the
    scalar tag values to disk in a vtk file.
    """

    index = 0
    while index < reference_length:
        scalar_data = []
        for tag in vector_tags:
            data = mb_ext.tag_get_data(tag, hexes_ext)
            scalar_data = np.copy(data[:,index])
            data_type = tag.get_data_type()
            scalar_tag = mb_ref.tag_get_handle(tag.get_name(), 1, data_type,
                                            types.MB_TAG_SPARSE, create_if_missing = True)
            mb_ref.tag_set_data(scalar_tag, hexes_ref, scalar_data)
        file_location = os.getcwd() + "/" + dir_name + "/" + tag_name + str(index) + ".vtk"
        mb_ref.write_file(file_location)
        index += 1

    print(str(index) + " files have been written to disk.")


def main():

    # Parse arguments.
    args = parse_arguments()

    # Expand the vector tags from the mesh file.
    tag_expansion(args.meshfile)


if __name__ == "__main__":
    main()
