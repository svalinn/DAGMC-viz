from visit import *
from PlotMesh import PlotMesh
from PlotContour import PlotContour
from PlotPseudocolor import PlotPseudocolor


class PlotSettings(object):
    """Visual settings for plots."""

    def __init__(self, myList):
        self.myList = myList

    def Pseudocolor(self):
        PlotPseudocolor(self.myList)

    def Contour(self):
        PlotContour(self.myList)

    def Mesh(self):
        PlotMesh(self.myList)
