import visit as Vi

Vi.LaunchNowin()  # Here to allow import of other modules.

import PathCreator as Pa
import PlotSettings as Pl
import OperatorSettings as Op
import WindowSettings as Wi
import Saving as Sa


class MakeImages:
    """Create images in visit."""

    def __init__(self, file, plot, vari):
        """Initializes MakeImages with default directory creation."""

        Pa.PathCreator()  # Creates necessary folders.

        self.file = file
        self.plot = plot
        self.vari = vari

    def Load(self):
        """Loads the data into VisIt."""

        Vi.OpenDatabase("./Data/"+self.file)
        Vi.AddPlot(self.plot, self.vari)

    def Plot(self):
        """Add desired plot settings."""

        Pl.PlotSettings()

    def Operator(self):
        """Add operator and it's settings."""

        Op.OperatorSettings()

    def Window(self):
        """Add window settings."""

        Wi.WindowSettings()

    def Saving(self):
        """Saves window image, python session, and HML session."""

        Sa.Saving()
