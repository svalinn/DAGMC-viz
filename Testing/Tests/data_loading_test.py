"""
This class ensures that DataLoading.py correctly produces a VisIt session file.
"""

import filecmp
import os
import visit
from xmldiff import main

from PythonTool.DataLoading import py_mb_convert, plane_slice_plotting, visit_config

# Choose the data files to be used during testing.
geom_file = "Testing/SampleData/donut.h5m"
mesh_file = "Testing/SampleData/meshtal.vtk"
plane_slice_session_file = "Testing/SampleData/VisitPlotData.session"
plane_slice_image = "Testing/SampleData/XYPlaneSlice.png"
session_file = "Testing/SampleData/VisitDefaultOutput.session"


def test_py_mb_convert():
    """
    Ensure this function returns the correct converted file name.
    """
    file_name = py_mb_convert(geom_file, ".stl")
    assert file_name == "donut.stl"


def test_plane_slice_plotting():
    """
    Ensure this function correctly generates a plane slice plot.
    """
    visit.LaunchNowin()
    visit.RestoreSession(plane_slice_session_file, 0)
    plane_slice_plotting(2, 2, "XY Plane", True, True)
    diff = filecmp.cmp("visit0000.png", plane_slice_image)
    assert diff == True
    visit.Close()


def test_visit_config():
    """
    Ensure that DataLoading.py correctly produces a VisIt session file.
    """
    os.system("python PythonTool/DataLoading.py %s %s -s -v" % (geom_file, mesh_file))
    diff = main.diff_files("VisitDefaultOutput.session", session_file)
    assert len(diff) == 4

"""
def test_cleanup():

    Remove the files written to disk by this class of tests.

    os.system('rm visit* *.stl *.vtk *.session')
"""
