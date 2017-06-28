from visit import *
from PlotMesh import PlotMesh
from PlotContour import PlotContour
from PlotPseudocolor import PlotPseudocolor


class PlotSettings(object):
    """Visual settings for plots."""

    def __init__(self, File):
        self.File = File

    def Pseudocolor(self):
        PlotPseudocolor()

    def Contour(self):
        PlotContour()

    def Mesh(self):
        PlotMesh()
