import argparse
import numpy as np
from pymoab import core, types, tag
from pymoab.types import MBENTITYSET

mb = core.Core()

parser = argparse.ArgumentParser(description="Remove graveyard from an h5m data file.")

parser.add_argument("h5mfile",
                    type=str, 
                    help='provide a path to the h5m data file'
                    )
parser.add_argument("-of", "--outputfile",
                    type=str, 
                    help='provide a name and extension for the output file'
                    )

args = parser.parse_args()

#Read the data file with the graveyard to be removed.
mb.load_file(args.h5mfile)

tag_name = mb.tag_get_handle("NAME")
tag_category = mb.tag_get_handle("CATEGORY")
root = mb.get_root_set()

#An array of tag values to be matched for entities returned by the following call.
group_tag_values = np.array(["Group"])

#Retrieve all EntitySets with a Category tag with the value of "Group".
group_categories = list(mb.get_entities_by_type_and_tag(root, MBENTITYSET, 
                                                        tag_category, group_tag_values))

#Retrieve all EntitySets with a Name tag.
group_names = mb.tag_get_data(tag_name, group_categories, flat=True)

#Find the EntitySet with the "graveyard" Name tag value.
graveyard_sets = [group_set for group_set, name in zip(group_categories, group_names) 
                  if name.lower() == b'graveyard']

#Print the EntityHandle of the EntitySet(s) with the "graveyard" Name tag value.
print(graveyard_sets)

if len(graveyard_sets) > 1:
    print("WARNING: More than one graveyard set found.")
    exit()

#Remove the graveyard EntitySet from the data.
groups_to_write = [group_set for group_set in group_categories 
                   if group_set not in graveyard_sets]

"""Check if the user specified an output file name.
If so, write the file with that name. If not, append onto 
the original input file name to indicate the graveyard has been removed.
"""

if args.outputfile is not None:
    mb.write_file(args.outputfile, output_sets=groups_to_write)
else:
    input_array = args.h5mfile.split("/")
    input_file = input_array[-1]
    input_file_name = input_file[:-4]    
    mb.write_file(input_file_name + "_no_grave.h5m", output_sets=groups_to_write)
