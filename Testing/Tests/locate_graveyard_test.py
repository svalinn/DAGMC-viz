"""
This test ensures that locate_graveyard() in GraveyardRemoval.py correctly identifies the graveyard volume.
"""

import sys

sys.path.insert(1,'/home/piperlincoln/CNERG/DAGMC-viz/PythonTool')
from GraveyardRemoval import get_sets_by_category
from GraveyardRemoval import locate_graveyard


def test_get_sets_by_category():

        # Check that this function returns the correct list of entity sets without the graveyard volume.
        groups_to_write = locate_graveyard('../SampleData/fng_zip.h5m')
        assert groups_to_write == [12682136550675320105, 12682136550675320106, 12682136550675320107, 12682136550675320108, 12682136550675320109, 12682136550675320110, 12682136550675320111]

