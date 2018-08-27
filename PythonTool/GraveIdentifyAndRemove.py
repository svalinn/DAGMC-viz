import numpy as np
from pymoab import core, types, tag
from sys import argv

mb=core.Core()

#Read the data file with the graveyard to be removed.
mb.load_file(argv[1])

tag_name=mb.tag_get_handle("NAME")
tag_category=mb.tag_get_handle("CATEGORY")
root=mb.get_root_set()

#Retrieve all EntitySets with a Category tag with a value of "Group".
group_es=list(mb.get_entities_by_type_and_tag(root,types.MBENTITYSET,
                                              tag_category, np.array(["Group"])))

#Retrieve all EntitySets with a Name tag.
group_names=mb.tag_get_data(tag_name,group_es,flat=True)

#Find the EntitySet with the "graveyard" Name tag value.
graveyard_sets=[group_set for group_set,name in zip(group_es,group_names) 
                if name.lower()==b'graveyard']
print(graveyard_sets)

if len(graveyard_sets) > 1:
    print("WARNING: More than one graveyard set found.")

#Remove the graveyard EntitySet from the data.
groups_to_write=[group_set for group_set in group_es if group_set not in graveyard_sets]
mb.write_file("no_graveyard.h5m",output_sets=groups_to_write)
