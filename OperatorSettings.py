from visit import *
from OperatorClip import OperatorClip
from OperatorSlice import OperatorSlice
from OperatorThreshold import OperatorThreshold


def OperatorSettings(OperSet, myList, Centroids, tags):
    """Add operator and its settings."""

    if OperSet == "Slice":
        OperatorSlice(myList)

    if OperSet == "Clip":
        OperatorClip(myList, Centroids)

    if OperSet == "Threshold":
        OperatorThreshold(myList, tags)
