"""
This class ensures that TagExpansion.py correctly expands all vector tags in a mesh.
"""

import os
import pymoab
import pytest

from PythonTool.TagExpansion import get_tag_lists, create_directory, expand_vec_tag

# Initialize a PyMOAB core instance and load in the h5m file.
data_file = "Testing/SampleData/photon_flux_mesh.h5m"
mb = pymoab.core.Core()
mb.load_file(data_file)


def test_get_tag_lists():
    """
    Ensure this function correctly retrieves all elements, scalar tags, and vector tags in a mesh.
    """
    elements, scalars, vectors = get_tag_lists(mb, "hex")
    assert (len(elements),len(scalars),len(vectors)) == (33750,3,2)


def test_get_tag_lists_exception():
    """
    Ensure this function correctly detects when there are none of a specified element in the mesh.
    """
    with pytest.raises(LookupError) as e:
        get_tag_lists(mb, "tet")


def test_create_directory():
    """
    Ensure this function correctly creates a new directory name for tag expansion.
    """
    os.mkdir("photon0")
    dir_name = create_directory("photon", False)
    assert dir_name == "photon1"


def test_create_directory_option():
    """
    Ensure this function correctly overwrites a directory name for tag expansion.
    """
    os.mkdir("photon10")
    dir_name = create_directory("photon1", True)
    assert dir_name == "photon10"


def test_expand_vec_tag():
    """
    Ensure this function correctly creates a scalar tag database for a given vector tag.
    """
    elements = mb.get_entities_by_type(mb.get_root_set(), pymoab.types.MBHEX)
    tag_list = mb.tag_get_tags_on_entity(elements[0])
    scal_tags = [tag_list[0], tag_list[3], tag_list[4]]
    vec_tag = tag_list[1]
    os.mkdir("photon_flux_mesh_database")
    expand_vec_tag(mb, elements, scal_tags, vec_tag, "photon_flux_mesh_database")
    path, dirs, files = next(os.walk("photon_flux_mesh_database/photon_result_database"))
    assert len(files) == 24


def test_tag_expansion():
    """
    Ensure that TagExpansion correctly expands all vector tags in a mesh.
    """
    os.system("python PythonTool/TagExpansion.py %s" % data_file)
    path, dirs, files = next(os.walk("photon_flux_mesh0/photon_result_database"))
    assert len(files) == 24


def test_cleanup():
    """
    Remove the files written to disk by this class of tests.
    """
    os.system("rm -rf photon*")
