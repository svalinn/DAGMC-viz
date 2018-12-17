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


def get_vector_tags(mb, element):
    """
    Create a list of each vector tag in the mesh file by identifying each tag on
    a specific mesh element and determining if it is vector or scalar.

    Input:
    ______
       mb: Core
           A PyMOAB core instance with a loaded data file.
       element: int
           The type of MOAB element from which to extract the tag list.

    Returns:
    ________
       element_list: List
           The list of all specific elements in the mesh.
       vector_tags: List
           A list of all vector tags in the mesh.
    """

    # Retrieve an arbitrary MBHEX element in the mesh and extract the tag list.
    root = mb.get_root_set()
    element_list = mb.get_entities_by_type(root, element)

    # If there are none of the specified mesh elements, print a warning and exit.
    if len(element_list) == 0:
        print("WARNING: No hex elements were found in this data file.")
        exit()

    tag_list = mb.tag_get_tags_on_entity(element_list[0])

    # Check if each tag is a vector. If so, append it to the list.
    vector_tags = []
    for tag in tag_list:
        tag_length = mb.tag_get_length(tag)
        if tag_length > 1:
            vector_tags.append(tag)

    return element_list, vector_tags


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

    # Retrieve the list of vector tags on the mesh.
    hexes_ref, vec_tags_ref = get_vector_tags(mb_ref, types.MBHEX)

    # Grab the length and name of the vector tag for later use.
    reference_length = vec_tags_ref[0].get_length()
    tag_name = vec_tags_ref[0].get_name()

    # Delete each vector tag from the reference mesh.
    for tag in vec_tags_ref:
        mb_ref.tag_delete(tag)

    # Load the mesh file for extracting vector tag data.
    mb_ext = core.Core()
    mb_ext.load_file(mesh_file)

    # Retrieve the list of vector tags on the mesh.
    hexes_ext, vec_tags_ext = get_vector_tags(mb_ext, types.MBHEX)

    # Ensure each vector tag is the same length.
    for tag in vec_tags_ext:
        if mb_ext.tag_get_length(tag) is not reference_length:
            print("WARNING: Found a vector tag of different length.")
            exit()

    # Make sure the mesh file contains at least one vector tag.
    if len(vec_tags_ext) < 1:
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
        for tag in vec_tags_ext:
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
