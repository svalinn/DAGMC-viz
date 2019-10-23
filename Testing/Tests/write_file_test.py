"""
This test ensures that write_file() in GraveyardRemoval.py writes the correct file to disk.
"""

import filecmp
import os
import sys

sys.path.insert(1,'/home/piperlincoln/CNERG/DAGMC-viz/PythonTool')
from GraveyardRemoval import locate_graveyard
from GraveyardRemoval import write_file


def test_get_sets_by_category():

        # Check that this function outputs the correct file.
	groups_to_write = locate_graveyard('../SampleData/fng_zip.h5m')
	output_file = write_file(groups_to_write, '../SampleData/fng_zip.h5m', 'output_file.vtk')
	result = filecmp.cmp('../SampleData/fng_zip_no_grave.vtk','output_file.vtk')
	assert result == True

	# Remove unwanted files.
	os.system('rm output_file.vtk')

