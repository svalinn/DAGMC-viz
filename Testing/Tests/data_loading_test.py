"""
This test ensures that DataLoading.py produces the correct VisIt session file.
"""

import os
import subprocess
import sys
import time


def test_data_loading():

	# Launch the script and wait for it to finish.
	process = subprocess.Popen(["python", "../../PythonTool/DataLoading.py",
                                    "../SampleData/fng_zip.h5m", "../SampleData/meshtal.vtk", "-v", "-s"])
	time.sleep(20)

	# Check if the VisIt session file was generated correctly.
	diff = os.system('echo diff VisitDefaultOutput.session ../SampleData/VisitDefaultOutput.session')
	assert diff == 0

	# Remove unwanted files.
	os.system('rm fng* meshtal* visit* *.session')
