import visit as Vi

import PathCreator as Pa
import PlotSettings as Pl
import SaveSessions as Sa
import WindowSettings as Wi
import OperatorSettings as Op
import PlotAndInformation as Qu


class MakeImages(object):
    """Create images in visit."""

    Pa.PathCreator()  # Creates necessary folders.

    def __init__(self, File):
        """Initializes MakeImages with default directory creation."""

        self.File = File

    def Plot(self):
        """Loads the data into VisIt."""

        # Get plot and get information from each plot type.
        PlotAndGetInfo = Qu.PlotAndInformation(self.File)
        self.PlottingSequence = PlotAndGetInfo[0]
        self.PlottingCentroids = PlotAndGetInfo[1]

        # Apply plot settings
        Apply = Pl.PlotSettings(self.File)

        for key in self.File:
            eval("Apply."+str(self.File[key][1])+"()")

    def Operator(self, OperSet, myList=None):
        """Set the settings for plots and operators."""

        Apply = Op.OperatorSettings(
                                    self.File,
                                    OperSet,
                                    myList,
                                    self.PlottingCentroids,
                                    self.PlottingSequence,
                                    )

        eval("Apply."+str(OperSet).title()+"()")

    def Save(self):
        """Saves window image and XML session."""

        Vi.DrawPlots()
        Wi.WindowSettings()
        Sa.SaveSessions()
        Vi.SaveWindow()
