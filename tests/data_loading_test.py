"""
This class ensures that DataLoading.py correctly produces a VisIt session file.
"""

import os
import pytest
import visit
from xmldiff import main

from svalinn_tools.data_loading import py_mb_convert, plane_slice_plotting, visit_config

# Choose the data files to be used during testing.
geom_file = "tests/files_graveyard_removal/donut.h5m"
mesh_file = "tests/files_data_loading/meshtal.vtk"
plane_slice_session_file = "tests/files_data_loading/VisitPlotData.session"
session_file = "tests/files_data_loading/VisitDefaultOutput.session"


def test_py_mb_convert():
    """
    Ensure this function returns the correct converted file name.
    """
    file_name = py_mb_convert(geom_file, ".stl")
    assert file_name == "donut.stl"


def test_plane_slice_plotting():
    """
    Ensure this function correctly generates three plane slice plots.
    """
    visit.LaunchNowin()
    visit.RestoreSession(plane_slice_session_file, 0)
    plane_slice_plotting(2, 2, "XY Plane", False, False)
    plane_slice_plotting(3, 1, "XZ Plane", False, False)
    plane_slice_plotting(4, 0, "ZY Plane", False, False)
    visit.SetWindowLayout(4)
    visit.SaveSession("PlaneSlice.session")
    diff = main.diff_files("PlaneSlice.session", session_file)
    assert len(diff) <= 105 # Accounts for bare minimum differences due to sources, hosts, etc.
    visit.Close()


def test_visit_config():
    """
    Ensure that DataLoading.py correctly produces a VisIt session file.
    """
    os.system("python svalinn_tools/data_loading.py %s %s -s -v" % (geom_file, mesh_file))
    diff = main.diff_files("VisitDefaultOutput.session", session_file)
    assert len(diff) <= 28 # Accounts for bare minimum differences due to sources, hosts, etc.


def test_cleanup():
    """
    Remove the files written to disk by this class of tests.
    """
    os.system('rm visit* *.stl *.vtk *.session')
