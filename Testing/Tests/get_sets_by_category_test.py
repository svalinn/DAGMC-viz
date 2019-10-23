"""
This test ensures that get_sets_by_category() in GraveyardRemoval.py returns the correct list of entity sets.
"""

import sys

sys.path.insert(1,'/home/piperlincoln/CNERG/DAGMC-viz/PythonTool')
from GraveyardRemoval import get_sets_by_category
from pymoab import core


def test_get_sets_by_category():

	# Check that this function returns the correct number of entities with the specified tag.
	mb = core.Core()
	mb.load_file('../SampleData/fng_zip.h5m')
	group_categories = get_sets_by_category(mb, "Group")
	assert len(group_categories) == 8
