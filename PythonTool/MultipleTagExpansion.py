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


def get_tag_lists(mb, element):
    """
    Create separate lists of each scalar and vector tag in the mesh file by
    identifying each tag on a specific mesh element and determining the type.

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
       scalar_tags: List
           A list of all scalar tags in the mesh.
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

    # Check the type of each tag and append to the appropriate list.
    scalar_tags = []
    vector_tags = []
    for tag in tag_list:
        tag_length = mb.tag_get_length(tag)
        if tag_length > 1:
            vector_tags.append(tag)
        else:
            scalar_tags.append(tag)

    return element_list, scalar_tags, vector_tags


def tag_expansion(mesh_file, mb, hexes, scal_tags, vec_tag, reference_length, tag_name):
    """
    Expand the vector tag on each element in the given mesh data file. Write a
    file to disk for each index with the corresponding scalar tag values.

    Input:
    ______
       mesh_file: str
           User supplied mesh file location.

    Returns:
    ________
       none
    """

    # Create a directory for the vector tag expansion files.
    input_list = mesh_file.split("/")
    file_name = '.'.join(input_list[-1].split(".")[:-1])
    dir_name = file_name + "_database"

    # Ensure an existing dictionary is not written over.
    dict_number = 1
    while os.path.isdir(dir_name):
        dir_name = file_name + "_database" + str(dict_number)
        dict_number += 1
    os.mkdir(dir_name)

    """
    For the vector tag on each element, retrieve the scalar value at a specific
    index and create a scalar tag. For each index, write the scalar tag values
    to disk in a vtk file in the specified database.
    """

    index = 0
    while index < reference_length:
        scalar_data = []
        data = mb.tag_get_data(vec_tag, hexes)
        scalar_data = np.copy(data[:,index])
        data_type = vec_tag.get_data_type()
        scalar_tag = mb.tag_get_handle(tag_name, 1, data_type, types.MB_TAG_SPARSE,
                                       create_if_missing = True)
        mb.tag_set_data(scalar_tag, hexes, scalar_data)

        # Append the new scalar tag onto the original list of scalar tags.
        scal_tags.append(scalar_tag)

        # Write the mesh file with the new scalar tag.
        file_location = os.getcwd() + "/" + dir_name + "/" + tag_name + str(index) + ".vtk"
        mb.write_file(file_location, tags = scal_tags)

        # Remove the new scalar tag from the original list to prepare to write the next.
        scal_tags = scal_tags[:-1]
        index += 1

    print(str(index) + " files have been written to disk.")


def load_mesh(mesh_file):
    """
    Load the mesh file and extract the lists of scalar and vector tags, then
    expand each vector tag.

    Input:
    ______
       mesh_file: str
           User supplied mesh file location.

    Returns:
    ________
       none
    """

    # Load the mesh file.
    mb = core.Core()
    mb.load_file(mesh_file)

    # Retrieve the lists of scalar and vector tags on the mesh.
    hexes, scal_tags, vec_tags = get_tag_lists(mb, types.MBHEX)

    # Make sure the mesh file contains at least one vector tag.
    if len(vec_tags) < 1:
        print("WARNING: This mesh file did not contain any vector tags.")
        exit()

    for tag in vec_tags:
        length = tag.get_length()
        name = tag.get_name()
        tag_expansion(mesh_file, mb, hexes, scal_tags, tag, length, name)


def main():

    # Parse arguments.
    args = parse_arguments()

    # Expand the vector tags from the mesh file.
    load_mesh(args.meshfile)


if __name__ == "__main__":
    main()
