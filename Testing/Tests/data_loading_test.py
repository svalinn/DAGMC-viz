"""
This class ensures that DataLoading.py correctly produces a VisIt session file.
"""

import filecmp
import os
import visit
from PythonTool.DataLoading import py_mb_convert, plane_slice_plotting, visit_config

# Choose the data files to be used during testing.
geom_file = "Testing/SampleData/donut.h5m"
mesh_file = "Testing/SampleData/meshtal.vtk"


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
    visit.RestoreSession("Testing/SampleData/VisitPlotData.session", 0)
    plane_slice_plotting(2, 2, "XY Plane", True, True)
    diff = filecmp.cmp("visit0000.png", "Testing/SampleData/XYPlaneSlice.png")
    assert diff == True
    visit.Close()


def test_visit_config():
    """
    Ensure that DataLoading.py correctly produces a VisIt session file.
    """
    os.system("python PythonTool/DataLoading.py %s %s -s -v" % (geom_file, mesh_file))
    diff = os.popen("sort VisitDefaultOutput.session Testing/SampleData/VisitDefaultOutput.session| uniq -u").read().split("\n")
    assert len(diff) == 9
    os.system('rm donut* meshtal* visit* *.session')
