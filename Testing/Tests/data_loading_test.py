"""
This class ensures that DataLoading.py correctly produces a VisIt session file.
"""

import filecmp
import os
import sys
import visit
from pymoab import core

sys.path.insert(1,"../../PythonTool")

from DataLoading import py_mb_convert, plane_slice_plotting, visit_config


def test_py_mb_convert():
	# Ensure this function returns the correct converted file name.
    file_name = py_mb_convert("../SampleData/donut.h5m", ".stl")
    assert file_name == "donut.stl"
    os.remove("donut.stl")


def test_plane_slice_plotting():
    # Ensure this function correctly generates a plane slice plot.
    visit.LaunchNowin()
    visit.RestoreSession("../SampleData/VisitPlotData.session",0)
    plane_slice_plotting(2, 2, "XY Plane", True, True)
    diff = filecmp.cmp("visit0000.png", "../SampleData/XYPlaneSlice.png")
    assert diff == True
    os.remove("visit0000.png")
    visit.Close()


def test_visit_config():
	# TODO
	assert True == True


def test_data_loading():
    # Ensure that DataLoading.py correctly produces a VisIt session file.
    os.system("python ../../PythonTool/DataLoading.py ../SampleData/donut.h5m ../SampleData/meshtal.vtk")
    diff = filecmp.cmp("VisitDefaultOutput.session", "../SampleData/VisitDefaultOutput.session")
    assert diff == True
    os.system('rm donut* meshtal* visit* *.session')
