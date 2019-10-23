"""
This test ensures that GraveyardRemoval.py prints the graveyard volume entity handle correctly.
"""

import os
import subprocess
import time


def test_graveyard_output_file():

	# Launch the script and wait for it to finish.
	handle = subprocess.check_output(["python", "../../PythonTool/GraveyardRemoval.py",
					  "../SampleData/fng_zip.h5m", "-p"])
	time.sleep(2)

	# Check that the correct entity handle was printed.
	assert ("12682136550675320112" in handle) == True

	# Remove unwanted files.
	os.system('rm fng_zip_no_grave.h5m')
