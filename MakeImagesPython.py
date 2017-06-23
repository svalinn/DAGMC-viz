import visit as Vi

# The next line can be commented to import and use in the VisIt GUI.
Vi.LaunchNowin()  # Here to allow import of other modules.

import PathCreator as Pa
import PlotSettings as Pl
import OperatorSettings as Op
import WindowSettings as Wi
import SaveSessions as Sa


class MakeImages(object):
    """Create images in visit."""

    Pa.PathCreator()  # Creates necessary folders.

    def __init__(self, file):
        """Initializes MakeImages with default directory creation.


        A python script with the name Inputs.py was used to specify the
        data, plot, and variable used. Operators were also defined. Within
        Inputs.py, is code similar to the dictionaries listed below:

        The following is an example of a valid input type for self.file:
           Files = {
                "Plot_1" : ["meshtal.vtk"]+["Pseudocolor"]+["TALLY_TAG"],
                "Plot_2" : ["meshtal.vtk"]+["Contour"]+["ERROR_TAG"],
                "Plot_3" : ["fng_zip.stl"]+["Mesh"]+["STL_mesh"],
                    }
        """

        self.file = file

    def Plot(self):
        """Loads the data into VisIt."""

        for key in self.file:
            Vi.OpenDatabase("./Data/"+self.file[key][0])
            Vi.AddPlot(self.file[key][1], self.file[key][2])

    def Operator(self, OperatorSet):
        """Add operator and it's settings."""

        Vi.RemoveAllOperators()

        if not OperatorSet == "None":
            Vi.AddOperator(str(OperatorSet), 1)

    def Settings(self, OperSet, myList):
        """Set the settings for plots and operators."""

        Pl.PlotSettings()

        if OperSet:
            Vi.SetActivePlots((tuple(range(0, len(self.file)))))
            Op.OperatorSettings(str(OperSet), myList)

    def Save(self):
        """Saves window image and XML session."""

        Vi.DrawPlots()
        Wi.WindowSettings()
        Sa.SaveSessions()
        Vi.SaveWindow()
