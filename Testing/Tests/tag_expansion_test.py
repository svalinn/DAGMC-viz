"""
This test ensures that TagExpansion.py expands all vector tags in a mesh to their respective scalar tags.
"""

import os
import subprocess
import time


def test_tag_expansion():

	# Launch the script and wait for it to finish.
	subprocess.Popen(["python", "../../PythonTool/TagExpansion.py",
                          "../SampleData/nflux_mesh.h5m", "-e", "tet"])
	time.sleep(60)

	# Check that the database has the appropriate number of files.
	path, dirs, files = next(os.walk("nflux_mesh_database/TALLY_TAG_database"))
	assert len(files) == 175

	# Remove unwanted files.
	os.system('rm -rf nflux_mesh_database')
