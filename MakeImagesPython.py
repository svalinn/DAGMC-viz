import argparse

import visit as Vi

Vi.LaunchNowin()  # Here to allow import of other modules.

import PathCreator as Pa
import PlotSettings as Pl
import OperatorSettings as Op
import WindowSettings as Wi
import Save as Sa

Pa.PathCreator()  # Creates necessary folders.


class MakeImages(object):
    """Create images in visit."""

    def __init__(self, file, plot, vari):
        """Initializes MakeImages with default directory creation."""

        self.file = file
        self.plot = plot
        self.vari = vari

    def Plot(self):
        """Loads the data into VisIt."""

        Vi.OpenDatabase("./Data/"+self.file)
        Vi.AddPlot(self.plot, self.vari)

    def Operator(self):
        """Add operator and it's settings."""

        Vi.AddOperator("Slice", 1)

    def Settings(self):
        """Set the settings for plots and operators."""

        Pl.PlotSettings()
        Op.OperatorSettings()

    def Save(self):
        """Saves window image, python session, and HML session."""

        Vi.DrawPlots()
        Wi.WindowSettings()
        Sa.Save()
