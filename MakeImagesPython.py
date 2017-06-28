import visit as Vi

# The next line can be commented to import and use in the VisIt GUI.
Vi.Launch()  # Here to allow import of other modules.

import PathCreator as Pa
import PlotSettings as Pl
import SaveSessions as Sa
import WindowSettings as Wi
import OperatorSettings as Op


class MakeImages(object):
    """Create images in visit."""

    Pa.PathCreator()  # Creates necessary folders.

    def __init__(self, File):
        """Initializes MakeImages with default directory creation.


        A python script with the name Inputs.py was used to specify the
        data, plot, and variable used. Operators were also defined. Within
        Inputs.py, is code similar to the dictionaries listed below:

        The following is an example of a valid input type for self.File:
           Files = {
                "Plot_1" : ["meshtal.vtk"]+["Pseudocolor"]+["TALLY_TAG"],
                "Plot_2" : ["meshtal.vtk"]+["Contour"]+["ERROR_TAG"],
                "Plot_3" : ["fng_zip.stl"]+["Mesh"]+["STL_mesh"],
                    }
        """

        self.File = File

    def Plot(self):
        """Loads the data into VisIt."""

        Count = 0
        PlotType = []
        Centroids = []
        plotnumber = []

        for key in self.File:
            Vi.OpenDatabase("./Data/"+self.File[key][0])
            Vi.AddPlot(self.File[key][1], self.File[key][2])

            PlotType.append(self.File[key][1])
            plotnumber.append(Count)  # Loading order.

            Vi.SetActivePlots(Count)
            Vi.DrawPlots()

            Vi.Query("Centroid")  # Centroid of selected plot.
            Centroids.append(Vi.GetQueryOutputValue())
            self.Centroids = Centroids

            Count += 1

        # Create dictionaries of plot information.
        PlottingSequence = dict(zip(PlotType, plotnumber))
        PlottingCentroids = dict(zip(PlotType, Centroids))

        self.PlottingSequence = PlottingSequence
        self.PlottingCentroids = PlottingCentroids

        Apply = Pl.PlotSettings(self.File)
        Apply.Pseudocolor()
        Apply.Contour()
        Apply.Mesh()

    def Operator(self, OperSet, myList=None):
        """Set the settings for plots and operators."""

        Apply = Op.OperatorSettings(
                                    self.File,
                                    OperSet,
                                    myList,
                                    self.PlottingCentroids,
                                    self.PlottingSequence,
                                    )

        eval("Apply."+str(OperSet)+"()")

    def Save(self):
        """Saves window image and XML session."""

        Vi.DrawPlots()
        Wi.WindowSettings()
        Sa.SaveSessions()
        Vi.SaveWindow()
