import argparse

import visit as Vi

Vi.LaunchNowin()  # Here to allow import of other modules.

import PathCreator as Pa
import PlotSettings as Pl
import OperatorSettings as Op
import WindowSettings as Wi
import Save as Sa


class MakeImages:
    """Create images in visit."""

    def __init__(self, file, plot, vari):
        """Initializes MakeImages with default directory creation."""

        Pa.PathCreator()  # Creates necessary folders.

        self.file = file
        self.plot = plot
        self.vari = vari

    def Plot(self):
        """Loads the data into VisIt."""

        Vi.OpenDatabase("./Data/"+self.file)
        Pl.PlotSettings()
        Vi.AddPlot(self.plot, self.vari)

    def Operator(self):
        """Add operator and it's settings."""

        Op.OperatorSettings()

    def Save(self):
        """Saves window image, python session, and HML session."""

        Wi.WindowSettings()
        Sa.Save()
