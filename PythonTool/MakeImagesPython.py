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
        self.ObjectSequence = PlotAndGetInfo[3]

        # Apply plot settings
        Apply = Pl.PlotSettings(self.File, self.ObjectSequence)

        for item in self.File:
            eval("Apply."+str(item[1])+"()")

    def Operator(self, OperSet, OperOptions=None, SliceProject=1):
        """Set the settings for operators."""

        Apply = Op.OperatorSettings(
                                    self.File,
                                    OperSet,
                                    OperOptions,
                                    self.PlottingCentroids,
                                    self.PlottingSequence,
                                    self.PlottingSpatialExtents,
                                    SliceProject,
                                    )

        eval("Apply."+str(OperSet).title()+"()")

    def Save(self, Shading=False, OtherSources=False):
        """Saves window image and XML session."""

        Vi.DrawPlots()  # Draw plots after plots and/or operators.
        Wi.WindowSettings(Shading)  # Set settings for saved image.
        Sa.SaveSessions()  # Save incrementally a session.
        Vi.SaveWindow()  # Save incrementally the wanted image.

        print("Plot order is:\n"+str(self.PlottingSequence))
        print("Centroids are:\n"+str(self.PlottingCentroids))
        print("Bounds are:\n"+str(self.PlottingSpatialExtents))
        print("Plot object names:\n"+str(self.ObjectSequence))

    def get_list(self):
        """Return acquired data. """

        return [
                self.PlottingSequence,
                self.PlottingCentroids,
                self.PlottingSpatialExtents,
                self.ObjectSequence,
                ]
