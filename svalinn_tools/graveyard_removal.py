import argparse
import numpy as np
import sys
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


def get_sets_by_category(mb, category_name):
    """
    Identify EntitySets in the given geometry based on a category tag value.

    Input:
    ______
       mb: Core
           A PyMOAB core instance with a loaded data file.
       category_name: str
           The category tag value of the EntitySets to identify.

    Returns:
    ________
       group_categories: List
           The ID list of the EntitySets specific to the chosen category tag value.
    """

    tag_category = mb.tag_get_handle(str(types.CATEGORY_TAG_NAME))
    root = mb.get_root_set()

    # An array of tag values to be matched for entities returned by the following call.
    group_tag_values = np.array([category_name])

    # Retrieve all EntitySets with a category tag of the user input value.
    group_categories = mb.get_entities_by_type_and_tag(root, MBENTITYSET,
                                                       tag_category, group_tag_values)

    return list(group_categories)


def locate_graveyard(mb):
    """
    Locate the graveyard volume in the data file.

    Input:
    ______
       mb: Core
           A PyMOAB core instance with a loaded data file.

    Returns:
    ________
       groups_to_write: List
           The list of EntitySets with the graveyard volume omitted.
       graveyard_sets: List
           The list of graveyard EntitySets.

    Raises:
    _______
       LookupError: If no graveyard EntitySet is found.
    """

    tag_name = mb.tag_get_handle(str(types.NAME_TAG_NAME))

    # Gather all entities with a category tag value of "Group".
    group_categories = get_sets_by_category(mb, "Group")

    # Retrieve all EntitySets with a name tag.
    group_names = mb.tag_get_data(tag_name, group_categories, flat=True)

    # Find the EntitySet whose name tag value contains "graveyard".
    substring = "graveyard"
    graveyard_sets = [group_set for group_set, name in zip(group_categories, group_names)
                      if substring in str(name.lower())]

    # Warn the user if there was more than one EntitySet with the "graveyard" name tag value.
    if len(graveyard_sets) > 1:
        print("WARNING: More than one graveyard set was found.")

    # Raise an exception if there was no graveyard EntitySet found.
    if len(graveyard_sets) < 1:
        raise LookupError("WARNING: The geometry file did not contain a graveyard.")

    # Remove the graveyard EntitySet from the data.
    groups_to_write = [group_set for group_set in group_categories
                       if group_set not in graveyard_sets]

    return groups_to_write, graveyard_sets


def format_file_name(input_file, output_file = None):
    """
    Determine the name of the file to write to disk.

    If the user has specified an output file name and extension, use this to
    write the file. If they haven't, append "_no_grave" onto the name of the
    input file and add the .h5m extension.

    Input:
    ______
       input_file: str
           User supplied data file location.
       output_file: str
           Optional user supplied output file name and extension.

    Returns:
    ________
       file_name: str
           The name of the file to write to disk.
    """

    if output_file is None:
        input_list = input_file.split("/")
        file_name = '.'.join(input_list[-1].split(".")[:-1])
        output_file = file_name + "_no_grave.h5m"

    return output_file


def main():

    args = parse_arguments()

    # Load the data file into MOAB.
    mb = core.Core()
    mb.load_file(args.h5mfile)

    # Remove the graveyard volume from the data.
    try:
        groups_to_write, graveyard_sets = locate_graveyard(mb)
    except LookupError, e:
        sys.exit(e.message)

    # If the user would like, print the graveyard entity handle.
    if args.printhandle:
        print("The entity handle(s) of the graveyard EntitySet(s): " + str(graveyard_sets))

    # Write the file out to disk.
    output_file = format_file_name(args.h5mfile, args.outputfile)
    mb.write_file(output_file, output_sets=groups_to_write)


if __name__ == "__main__":
    main()
