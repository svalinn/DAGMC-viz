"""
This class ensures that GraveyardRemoval.py correctly removes the graveyard from an h5m file.
"""

import pymoab
import sys

sys.path.insert(1,"/home/piperlincoln/CNERG/DAGMC-viz/PythonTool")

from GraveyardRemoval import get_sets_by_category
from GraveyardRemoval import locate_graveyard
from GraveyardRemoval import format_file_name


"Initialize a PyMOAB core instance and load in the h5m data file."
mb = pymoab.core.Core()
mb.load_file("../SampleData/fng_zip.h5m")


def test_get_sets_by_category():
	# Ensure this function returns the correct number of entities with the specified tag.
    group_categories = get_sets_by_category(mb, "Group")
    assert len(group_categories) == 8


def test_default_locate_graveyard():
	# Ensure this function returns the correct list of entity sets without the graveyard volume.
    groups_to_write = locate_graveyard(mb)
    assert groups_to_write == [12682136550675320105, 12682136550675320106,
							   12682136550675320107, 12682136550675320108,
							   12682136550675320109, 12682136550675320110,
							   12682136550675320111]


def test_print_locate_graveyard(capsys):
	# Ensure this function prints the correct entity handle for the graveyard volume.
	groups_to_write = locate_graveyard(mb, True)
	out, err = capsys.readouterr()
	assert ("12682136550675320112" in out) == True


def test_default_format_file_name():
    # Ensure this function returns the correct default output file name.
    output_name = format_file_name('fng_zip.h5m')
    assert (output_name == 'fng_zip_no_grave.h5m') == True


def test_option_format_file_name():
    # Ensure this function returns the correct user input file name.
    output_name = format_file_name('fng_zip.h5m', 'test_output.h5m')
    assert (output_name == 'test_output.h5m') == True
