import visit as Vi

# The next line can be commented to import and use in the VisIt GUI.
Vi.LaunchNowin()  # Here to allow import of other modules.

import PathCreator as Pa
import PlotSettings as Pl
import OperatorSettings as Op
import WindowSettings as Wi
import SaveSessions as Sa

Pa.PathCreator()  # Creates necessary folders.


class MakeImages(object):
    """Create images in visit."""

    def __init__(self, file, oper):
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

            The following is an example of a valid input type for self.oper:
            Operators = {
                "Operator_1" : ["Slice"]+["1"],
               }
        """

        self.file = file
        self.oper = oper

    def Plot(self):
        """Loads the data into VisIt."""

        for key in self.file:
            Vi.OpenDatabase("./Data/"+self.file[key][0])
            Vi.AddPlot(self.file[key][1], self.file[key][2])

    def Operator(self):
        """Add operator and it's settings."""

        for key in self.oper:
            Vi.AddOperator(self.oper[key][0], int(self.oper[key][1]))

    def Settings(self):
        """Set the settings for plots and operators."""

        Pl.PlotSettings()

        # Applies the operator to all plots.
        # If the tuple in documentation worked, then the following:
        # Vi.SetActivePlots((tuple(range(0,len(Files)))))
        Number = 0
        for file in self.file:
            Vi.SetActivePlots(Number)
            Number += 1
            Op.OperatorSettings()

    def Save(self):
        """Saves window image, python session, and HML session."""

        Vi.DrawPlots()
        Wi.WindowSettings()
        Sa.SaveSessions()
        Vi.SaveWindow()
