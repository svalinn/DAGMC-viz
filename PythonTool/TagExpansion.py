import argparse
import numpy as np
import os
import sys
from pymoab import core, tag, types

# Create a dictionary with the MB element types and their integer values.
elements = {
    "vertex" : types.MBVERTEX,
    "edge" : types.MBEDGE,
    "tri" : types.MBTRI,
    "quad" : types.MBQUAD,
    "polygon" : types.MBPOLYGON,
    "tet" : types.MBTET,
    "pyramid" : types.MBPYRAMID,
    "prism" : types.MBPRISM,
    "knife" : types.MBKNIFE,
    "hex" : types.MBHEX,
    "polyhedron" : types.MBPOLYHEDRON,
    "entityset" : types.MBENTITYSET,
    "maxtype" : types.MBMAXTYPE
}


def parse_arguments():
    """
    Parse the argument list and return a mesh file location, optional main
    directory name, and optional MB element type.

    Input:
    ______
       none

    Returns:
    ________
       args: Namespace
           User supplied mesh file location, optional main directory name, and
           optional MB element type.
    """

    parser = argparse.ArgumentParser(description="Expand vector tags to scalar tags.")

    parser.add_argument("meshfile",
                        type=str,
                        help="Provide a path to the mesh file."
                        )
    parser.add_argument("-d", "--dirname",
                        type=str,
                        help="Provide a name for the main directory."
                        )
    parser.add_argument("-o", "--overwrite",
                        action="store_true",
                        help="Indicate whether to overwrite a directory from a previous expansion."
                        )
    parser.add_argument("-e", "--element",
                        type=str.lower,
                        default="hex",
                        choices=elements.keys(),
                        help="Provide the type of MOAB element on which to expand tags."
                        )

    args = parser.parse_args()

    # Determine the default name of the directory if none was supplied by the user.
    if args.dirname is None:
        args.dirname = '.'.join(args.meshfile.split("/")[-1].split(".")[:-1])

    return args


def get_tag_lists(mb, element_type):
    """
    Create separate lists of each scalar and vector tag in the mesh file by
    identifying each tag on a representative mesh element and determining the type.

    Input:
    ______
       mb: Core
           A PyMOAB core instance with a loaded data file.
       element_type: str
           The type of MOAB element from which to extract the tag list
           represented by a string.

    Returns:
    ________
       element_list: List of MOAB Entity Handles
           A list of all specific elements in the mesh, in which the type is
           represented by an integer.
       scalar_tags: List of PyMOAB Tags
           A list of all scalar tags in the mesh.
       vector_tags: List of PyMOAB Tags
           A list of all vector tags in the mesh.

    Raises:
    _______
       LookupError: If no element of the user specified type is found.
    """

    # Retrieve arbitrary element of specified type in the mesh and extract the tag list.
    global elements
    root = mb.get_root_set()
    element_list = mb.get_entities_by_type(root, elements[element_type])

    # Warn the user if there are none of the specified mesh elements.
    if len(element_list) == 0:
        raise LookupError("WARNING: No {} elements were found in the mesh.".format(element_type))

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


def create_directory(dir_name, overwrite):
    """
    Create a directory name for the vector tag expansion.

    Input:
    ______
       dir_name: str
           Name for main directory.
       overwrite: boolean
           Whether or not to overwrite a directory from a previous expansion.

    Returns:
    ________
       dir_name: str
           The name of the directory in which to create and populate each
           vector tag directory.
    """

    # If indicated by the user, ensure an existing directory is not written over.
    dict_number = 0
    if not overwrite:
        while os.path.isdir(dir_name + str(dict_number)):
            dict_number += 1

    # Create the directory name.
    dir_name = dir_name + str(dict_number)

    return dir_name


def expand_vec_tag(mb, elements, scal_tags, vec_tag, dir_name):
    """
    Expand the vector tag on each element in the given mesh data file. Write a
    file to disk for each index with the corresponding scalar tag value.

    Input:
    ______
       mb: Core
           A PyMOAB core instance with a loaded data file.
       elements: List of MOAB Entity Handles
           A list of all elements of a specific type in the mesh.
       scal_tags: List of PyMOAB Tags
           A list of all scalar tags in the mesh.
       vec_tag: PyMOAB Tag
           The vector tag to be expanded.
       dir_name: str
           The name of the directory in which to create and populate each
           vector tag directory.

    Returns:
    ________
       none
    """

    # Get the length, tag name, and data type of the vector tag.
    length = vec_tag.get_length()
    name = vec_tag.get_name()
    data_type = vec_tag.get_data_type()
    data = mb.tag_get_data(vec_tag, elements)

    # Create a directory to store the vector tag expansion files.
    try:
        vec_dir_name = dir_name + "/" + name + "_database"
        os.mkdir(vec_dir_name)
    except OSError:
        pass

    # Create the scalar tag template for the vector tag.
    scalar_tag = mb.tag_get_handle(str(name + "_exp"), 1, data_type, types.MB_TAG_SPARSE,
                                   create_if_missing = True)

    """
    For the vector tag on each element, retrieve the scalar value at a specific
    index and create a scalar tag. For each index, write the scalar tag value
    to disk in a vtk file in the specified database.
    """

    for index in range(0,length):
        scalar_data = []
        scalar_data = np.copy(data[:,index])
        mb.tag_set_data(scalar_tag, elements, scalar_data)

        # Write the mesh file with the new scalar tag.
        file_location = os.getcwd() + "/" + vec_dir_name + "/" + name + str(index) + ".vtk"
        scal_tags.append(scalar_tag)
        mb.write_file(file_location, output_tags = scal_tags)

        # Remove the new scalar tag from the list to prepare to write the next file.
        scal_tags = scal_tags[:-1]
        index += 1

    print(str(index) + " files have been written to disk.")


def main():

    args = parse_arguments()

    # Load the mesh file.
    mb = core.Core()
    mb.load_file(args.meshfile)

    # Retrieve the lists of scalar and vector tags on the mesh.
    try:
        elements, scal_tags, vec_tags = get_tag_lists(mb, args.element)
    except LookupError as e:
        sys.exit(str(e))

    # Warn the user if the mesh file does not contain at least one vector tag.
    if len(vec_tags) < 1:
        raise ValueError("WARNING: This mesh file did not contain any vector tags on {} elements.".format(args.element))

    # Create a directory to store vector tag expansion files.
    try:
        dir_name = create_directory(args.dirname, args.overwrite)
        os.mkdir(dir_name)
    except OSError:
        pass

    # Expand each vector tag present in the mesh.
    for tag in vec_tags:
        expand_vec_tag(mb, elements, scal_tags, tag, dir_name)


if __name__ == "__main__":
    main()
