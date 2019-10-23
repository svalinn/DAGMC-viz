"""
This test ensures that GraveyardRemoval.py names the output file correctly.
"""

import os
import subprocess
import time


def test_graveyard_output_file():

	# Launch the script and wait for it to finish.
	subprocess.Popen(["python", "../../PythonTool/GraveyardRemoval.py",
		          "../SampleData/fng_zip.h5m", "-o", "test_output.h5m"])
	time.sleep(2)

	# Check that the output file was named correctly.
	file = os.path.exists('test_output.h5m')
	assert file == True

	# Remove unwanted files.
	os.system('rm test_output.h5m')
