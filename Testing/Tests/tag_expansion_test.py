"""
This class ensures that TagExpansion.py correctly expands all vector tags in a mesh.
"""

import filecmp
import os
import pymoab
import pytest

from PythonTool.TagExpansion import get_tag_lists, create_directory, expand_vec_tag

# Initialize a PyMOAB core instance and load in the h5m file.
data_file = "Testing/SampleData/simple_mesh.h5m"
mb = pymoab.core.Core()
mb.load_file(data_file)


def test_get_tag_lists():
    """
    Ensure this function correctly retrieves all elements, scalar tags, and vector tags in a mesh.
    """
    elements, scalars, vectors = get_tag_lists(mb, "hex")
    assert (len(elements),len(scalars),len(vectors)) == (8,3,2)


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
    os.mkdir("simple_mesh0")
    dir_name = create_directory("simple_mesh", False)
    assert dir_name == "simple_mesh1"


def test_create_directory_option():
    """
    Ensure this function correctly overwrites a directory name for tag expansion.
    """
    os.mkdir("simple_mesh10")
    dir_name = create_directory("simple_mesh1", True)
    assert dir_name == "simple_mesh10"


def test_expand_vec_tag():
    """
    Ensure this function correctly creates a scalar tag database for a given vector tag.
    """
    elements = mb.get_entities_by_type(mb.get_root_set(), pymoab.types.MBHEX)
    tag_list = mb.tag_get_tags_on_entity(elements[0])
    scal_tags = [tag_list[0], tag_list[3], tag_list[4]]
    vec_tag = tag_list[1], tag_list[2]
    os.mkdir("simple_mesh")
    expand_vec_tag(mb, elements, scal_tags, vec_tag[0], "simple_mesh")
    expand_vec_tag(mb, elements, scal_tags, vec_tag[1], "simple_mesh")
    diff = filecmp.dircmp("simple_mesh", "Testing/SampleData/simple_mesh_expansion")
    assert len(diff.diff_files) == 0


def test_cleanup():
    """
    Remove the files written to disk by this class of tests.
    """
    os.system("rm -rf simple*")
