"""
This class ensures that GraveyardRemoval.py correctly removes the graveyard from an h5m file.
"""

import os
from pymoab import core

from scripts.graveyard_removal import get_sets_by_category, locate_graveyard, format_file_name

# Initialize a PyMOAB core instance and load in the h5m file.
test_file = "donut.h5m"
test_file_path = "tests/files_graveyard_removal/"
mb = core.Core()
mb.load_file(test_file_path + test_file)


def test_get_sets_by_category():
	"""
    Ensure this function returns the correct number of entities with the specified tag.
    """
	group_categories = get_sets_by_category(mb, "Group")
	assert len(group_categories) == 5


def test_locate_graveyard():
    """
    Ensure this function returns the correct list of entity sets without the graveyard volume.
    """
    groups_to_write, graveyard_sets = locate_graveyard(mb)
    assert groups_to_write == [12682136550675318125, 12682136550675318126,
                               12682136550675318128, 12682136550675318129]


def test_default_format_file_name():
	"""
    Ensure this function returns the correct default output file name.
    """
	output_name = format_file_name(test_file)
	assert (output_name == test_file[:-4] + "_no_grave.h5m") == True


def test_option_format_file_name():
	"""
    Ensure this function returns the correct user input file name.
    """
	output_name = format_file_name(test_file, 'test_output.h5m')
	assert (output_name == 'test_output.h5m') == True


def test_default_graveyard_removal():
	"""
    Ensure that GraveyardRemoval correctly removes the graveyard from an h5m file.
    """
	os.system("python scripts/graveyard_removal.py " + test_file_path + test_file)
	size = os.path.getsize(test_file[:-4] + "_no_grave.h5m")
	assert size == 5748780


def test_print_graveyard_removal(capfd):
    """
    Ensure that GraveyardRemoval prints the correct entity handle for the graveyard volume.
    """
    os.system("python scripts/graveyard_removal.py " + test_file_path + test_file + " -p")
    out, err = capfd.readouterr()
    assert ("12682136550675318127" in out) == True


def test_cleanup():
    """
    Remove the files written to disk by this class of tests.
    """
    os.remove(test_file[:-4] + "_no_grave.h5m")
