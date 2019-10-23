import argparse
import numpy as np
from pymoab import core, tag, types
from pymoab.types import MBENTITYSET


def parse_arguments():
    """
    Parse the argument list and return an input file location, an optional
    output file name, and whether or not to print the entity handle of the
    EntitySet with the "graveyard" name tag value.

    Input:
    ______
       none

    Returns:
    ________
       args: Namespace
           User supplied input file location, optional output file name, and
           whether or not to print the graveyard entity handle.
    """

    parser = argparse.ArgumentParser(description="Remove graveyard from an h5m data file.")

    parser.add_argument("h5mfile",
                        type=str,
                        help="Provide a path to the h5m data file."
                        )
    parser.add_argument("-o", "--outputfile",
                        type=str,
                        help="Provide a name and extension for the output file."
                        )
    parser.add_argument("-p", "--printhandle",
                        action="store_true",
                        help="Whether or not to print the graveyard entity handle."
                        )

    args = parser.parse_args()

    return args


def get_sets_by_category(mb_core, category_name):
    """
    Identify EntitySets in the given geometry based on a category tag value.

    Input:
    ______
       mb_core: Core
           A PyMOAB core instance with a loaded data file.
       category_name: str
           The category tag value of the EntitySets to identify.

    Returns:
    ________
       entity_set_ids: List
           The ID list of the EntitySets specific to the chosen category tag value.
    """

    tag_category = mb_core.tag_get_handle(str(types.CATEGORY_TAG_NAME))
    root = mb_core.get_root_set()

    # An array of tag values to be matched for entities returned by the following call.
    group_tag_values = np.array([category_name])

    # Retrieve all EntitySets with a category tag of the user input value.
    group_categories = mb_core.get_entities_by_type_and_tag(root, MBENTITYSET,
                                                            tag_category, group_tag_values)

    return list(group_categories)


def locate_graveyard(input_file, print_handle = None):
    """
    Locate and remove the graveyard volume from the data file. If the user has
    indicated to, print the handle of the EntitySet with the "graveyard" name tag value.

    Input:
    ______
       input_file: str
           User supplied data file location.
       print_handle: boolean
           Indicates whether or not to print the graveyard entity handle.

    Returns:
    ________
       groups_to_write: List
           The list of EntitySets with the graveyard volume omitted.

    Raises:
    _______
       LookupError: If no graveyard EntitySet is found.
    """

    mb = core.Core()
    mb.load_file(input_file)
    tag_name = mb.tag_get_handle(str(types.NAME_TAG_NAME))

    # Gather all entities with a category tag value of "Group".
    group_categories = get_sets_by_category(mb, "Group")

    # Retrieve all EntitySets with a name tag.
    group_names = mb.tag_get_data(tag_name, group_categories, flat=True)

    # Find the EntitySet whose name tag value contains "graveyard".
    graveyard_sets = [group_set for group_set, name in zip(group_categories, group_names)
                      if "graveyard" in str(name.lower())]

    # Warn the user if there was more than one EntitySet with the "graveyard" name tag value.
    if len(graveyard_sets) > 1:
        print("WARNING: More than one graveyard set was found.")

    # Raise an exception if there was no graveyard EntitySet found.
    if len(graveyard_sets) < 1:
        raise LookupError("WARNING: The geometry file did not contain a graveyard.")

    # If the user would like, print the graveyard entity handle.
    if print_handle:
        print("The entity handle(s) of the graveyard EntitySet(s): ")
        print(graveyard_sets)

    # Remove the graveyard EntitySet from the data.
    groups_to_write = [group_set for group_set in group_categories
                       if group_set not in graveyard_sets]

    return groups_to_write


def write_file(groups_to_write, input_file, output_file = None):
    """
    Write the new file to disk with a default input name or specific output name.

    If the user has specified an output file name and extension, use this to
    write the file. If they haven't, append "_no_grave" onto the name of the
    input file and add the .h5m extension.

    Input:
    ______
       groups_to_write: List
           The list of EntitySets with the graveyard volume omitted.
       input_file: str
           User supplied data file location.
       output_file: str
           Optional user supplied output file name and extension.

    Returns:
    ________
       output_file: str
           The name of the file written to disk.
    """

    mb = core.Core()
    mb.load_file(input_file)

    if output_file is not None:
        mb.write_file(output_file, output_sets=groups_to_write)
    else:
        input_list = input_file.split("/")
        file_name = '.'.join(input_list[-1].split(".")[:-1])
        output_file = file_name + "_no_grave.h5m"
        mb.write_file(output_file, output_sets=groups_to_write)

    return output_file


def main():

    args = parse_arguments()

    # Remove the graveyard volume from the data and write the updated file to disk.
    try:
        groups_to_write = locate_graveyard(args.h5mfile, args.printhandle)
    except LookupError, e:
        print(e.message)

    output_file = write_file(groups_to_write, args.h5mfile, args.outputfile)


if __name__ == "__main__":
    main()
