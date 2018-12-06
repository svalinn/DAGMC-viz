import argparse
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
    Expand vector tags to scalar tags in the given mesh data file and write the
    result for each vector tag to disk with a vtk extension.

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

    # Load the mesh file.
    mb = core.Core()
    mb.load_file(mesh_file)

    # Retrieve the MBHEX EntitySet(s) in the mesh.
    root = mb.get_root_set()
    hexes = mb.get_entities_by_type(root, types.MBHEX)

    if len(hexes) == 0:
        print("WARNING: No hex elements were found in this data file.")
        exit()

    # Retrieve an arbitrary MBHEX element and extract the tag list.
    tag_list = mb.tag_get_tags_on_entity(hexes[0])

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
                    base_file_name = "vector_data_"

                # Write a file with the scalar values from each vector tag expansion.
                file = open(base_file_name + str(i) + ".vtk","w")
                j = 0
                while j < len(vector):
                    scal_tag_j = vector[j]
                    file.write(str(scal_tag_j) + "\n")
                    j +=1
                i += 1

    print(str(len(data)) + " vector tags have been expanded and written to disk.")


def main():

    # Parse arguments.
    args = parse_arguments()

    # Expand the vector tags from the data file and write each to disk.
    tag_expansion(args.meshfile, args.outputfile, args.tags)


if __name__ == "__main__":
    main()
