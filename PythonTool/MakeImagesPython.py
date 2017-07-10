import visit as Vi

import PlotSettings as Pl
import SaveSessions as Sa
import WindowSettings as Wi
import OperatorSettings as Op
import PlotAndInformation as Qu


class MakeImages(object):
    """Create images in visit."""

    def __init__(self, File):
        """Initializes MakeImages with default directory creation."""

        self.File = File

    def Plot(self):
        """Loads the data into VisIt."""

        # Get plot and get information from each plot type.
        PlotAndGetInfo = Qu.PlotAndInformation(self.File)
        self.PlottingSequence = PlotAndGetInfo[0]
        self.PlottingCentroids = PlotAndGetInfo[1]
        self.PlottingSpatialExtents = PlotAndGetInfo[2]

        # Apply plot settings
        Apply = Pl.PlotSettings(self.File)

        for item in self.File:
            eval("Apply."+str(item[1])+"()")

    def Operator(self, OperSet, myList=None, SliceProject=1):
        """Set the settings for operators."""

        Apply = Op.OperatorSettings(
                                    self.File,
                                    OperSet,
                                    myList,
                                    self.PlottingCentroids,
                                    self.PlottingSequence,
                                    SliceProject,
                                    )

        eval("Apply."+str(OperSet).title()+"()")

    def Save(self, Shading=False):
        """Saves window image and XML session."""

        Vi.DrawPlots()
        Wi.WindowSettings(Shading)
        Sa.SaveSessions()
        Vi.SaveWindow()

    def get_list(self):
        """Return acquired data. """

        return [
                self.PlottingSequence,
                self.PlottingCentroids,
                self.PlottingSpatialExtents,
                ]
