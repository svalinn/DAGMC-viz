from visit import *
from OperatorClip import OperatorClip
from OperatorSlice import OperatorSlice
from OperatorThreshold import OperatorThreshold


class OperatorSettings(object):
    """Add operator and its settings."""

    def __init__(self, myList, Centroids, tags):

        self.tags = tags
        self.myList = myList
        self.Centroids = Centroids

    def Slice(self):
        OperatorSlice(self.myList)

    def Clip(self):
        OperatorClip(self.myList, self.Centroids)

    def Threshold(self):
        OperatorThreshold(self.myList, self.tags)
