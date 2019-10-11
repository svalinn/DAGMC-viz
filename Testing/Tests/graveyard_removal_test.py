"""
This test ensures that GraveyardRemoval.py removes the graveyard from an h5m file.
"""

import os
import subprocess
import time


def test_graveyard_removal():

	# Launch the script and wait for it to finish.
	subprocess.Popen(["python", "../../PythonTool/GraveyardRemoval.py", "../SampleData/fng_zip.h5m"])
	time.sleep(2)

	# Check that the file  is the correct size after the graveyard is removed.
	size = os.path.getsize('fng_zip_no_grave.h5m')
	assert size == 53390316

	# Remove unwanted files.
	os.system('rm fng_zip_no_grave.h5m')
