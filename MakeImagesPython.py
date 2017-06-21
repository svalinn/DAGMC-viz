import visit as Vi

# The next line can be commented to import and use in the VisIt GUI.
Vi.LaunchNowin()  # Here to allow import of other modules.

import PathCreator as Pa
import PlotSettings as Pl
import Operators as Oper
import OperatorSettings as OpSe
import WindowSettings as Wi
import SaveSessions as Sa

Pa.PathCreator()  # Creates necessary folders.


class MakeImages(object):
    """Create images in visit."""

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

        Oper.Operators(OperatorSet)

    def Settings(self, OperatorSet):
        """Set the settings for plots and operators."""

        Pl.PlotSettings()

        if OperatorSet:

            # Applies the operator to all plots.
            # If the tuple in documentation worked, then the following:
            # Vi.SetActivePlots((tuple(range(0,len(Files)))))
            Number = 0
            for file in self.file:
                Vi.SetActivePlots(Number)
                Number += 1
                OpSe.OperatorSettings(OperatorSet)

    def Save(self, Coordinates = (30.0, 30.0, 30.0)):
        """Saves window image, python session, and HML session."""

        Vi.DrawPlots()
        Wi.WindowSettings(Coordinates)
        Sa.SaveSessions()
        Vi.SaveWindow()
