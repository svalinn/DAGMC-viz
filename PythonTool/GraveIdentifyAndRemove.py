import argparse
import numpy as np
from pymoab import core, tag, types
from pymoab.types import MBENTITYSET


def parse_arguments():
    """
    Parse the argument list and return an input file location, an optional
    output file name, and indication of whether or not to print the entity handle
    of the EntitySet with the "graveyard" Name tag value.

    Input:
    ______
       none

    Returns:
    ________
       args: Namespace
           User supplied input file location, optional output file name, and
           indication of whether or not to print the graveyard entity handle.
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
                        help="Indicates whether or not to print the graveyard entity handle."
                        )

    args = parser.parse_args()

    return args


def get_sets_by_category(mb_core, category_name):
    """
    Identify EntitySets in the given geometry based on a Category tag value.

    Input:
    ______
       mb_core: Core
           A PyMOAB core instance with a loaded data file.
       category_name: str
           The Category tag value of the EntitySets to identify.

    Returns:
    ________
       entity_set_ids: List
           The ID list of the EntitySets specific to the chosen Category tag value.
    """

    tag_category = mb_core.tag_get_handle(str(types.CATEGORY_TAG_NAME))
    root = mb_core.get_root_set()

    # An array of tag values to be matched for entities returned by the following call.
    group_tag_values = np.array([category_name])

    # Retrieve all EntitySets with a Category tag of the user input value.
    group_categories = mb_core.get_entities_by_type_and_tag(root, MBENTITYSET,
                                                            tag_category, group_tag_values)
    group_categories = list(group_categories)

    return group_categories


def remove_graveyard(input_file, output_file = None, print_handle = None):
    """
    Remove the graveyard volume from the data file and write the result
    out to disk with a default input name or specified output name.

    If the user has specified an output file name and extension, use this to
    write the file. If they haven't, append "_no_grave" onto the name of the
    input file and add the .h5m extension.

    If the user has indicated to, print the entity handle of the EntitySet with
    the "graveyard" Name tag value.

    Input:
    ______
       input_file: str
           User supplied data file location.
       output_file: str
           Optional user supplied output file name and extension.
       print_handle: boolean
           Indicates whether or not to print the graveyard entity handle.

    Returns:
    ________
       output_file: str
           The name of the file written to the disk.

    Raises:
    _______
       LookupError: If no graveyard EntitySet is found.
    """

    mb = core.Core()

    # Read the data file with the graveyard to be removed.
    mb.load_file(input_file)

    tag_name = mb.tag_get_handle(str(types.NAME_TAG_NAME))

    # Gather all entities with a Category tag value of "Group".
    group_categories = get_sets_by_category(mb, "Group")

    # Retrieve all EntitySets with a Name tag.
    group_names = mb.tag_get_data(tag_name, group_categories, flat=True)

    # Find the EntitySet whose Name tag value contains "graveyard".
    substring = "graveyard"
    graveyard_sets = [group_set for group_set, name in zip(group_categories, group_names)
                      if substring in str(name.lower())]

    # Warn the user if there was more than one EntitySet with the "graveyard" Name tag value.
    if len(graveyard_sets) > 1:
        print("WARNING: More than one graveyard set found.")

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

    """
    Check if the user specified an output file name.
    If so, write the file with that name. If not, append onto
    the original input file name to indicate the graveyard has been removed.
    """

    if output_file is not None:
        mb.write_file(output_file, output_sets=groups_to_write)
    else:
        input_list = input_file.split("/")
        file_name = str(input_list[-1]).split(".")
        base_file_name = file_name[0]
        output_file = base_file_name + "_no_grave.h5m"
        mb.write_file(output_file, output_sets=groups_to_write)

    return output_file


def main():

    # Parse arguments.
    args = parse_arguments()

    # Remove the graveyard from the data file.
    try:
        output_file = remove_graveyard(args.h5mfile, args.outputfile, args.printhandle)
    except LookupError, e:
        print(e.message)


if __name__ == "__main__":
    main()
