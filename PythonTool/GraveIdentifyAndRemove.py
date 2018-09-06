import numpy as np
from pymoab import core, types, tag
from pymoab.types import MBENTITYSET
from sys import argv

mb = core.Core()

#Read the data file with the graveyard to be removed.
mb.load_file(argv[1])

tag_name = mb.tag_get_handle("NAME")
tag_category = mb.tag_get_handle("CATEGORY")
root = mb.get_root_set()

#An array of Tag values to be matched for entities returned by the following call.
group_tag_values = np.array(["Group"])

#Retrieve all EntitySets with a Category tag with a value of "Group".
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

#Remove the graveyard EntitySet from the data.
groups_to_write = [group_set for group_set in group_categories if group_set not in graveyard_sets]
mb.write_file("no_graveyard.h5m", output_sets=groups_to_write)
