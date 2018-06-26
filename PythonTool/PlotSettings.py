from visit import *

from Plots import *


class PlotSettings(object):
    """Visual settings for plots."""

    def __init__(self, File, ObjectSequence):
        self.File = File
        self.ObjectSequence = ObjectSequence

    def Pseudocolor(self):
        PlotPseudocolor(self.File, self.ObjectSequence)

    def Contour(self):
        PlotContour(self.File, self.ObjectSequence)

    def Mesh(self):
        PlotMesh(self.File)
