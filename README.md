Outdated Documentation


DAGMC-viz Documentation
=======================

(Note: Python 2.7 and visit are required. Python path needs to be set for visit.)

There are three primary methods of use for this tool.

1. MakeImagesTerminal.py can be used to load data. The following is an example input that loads data (-p) and applies an operator (-o):
	
		python MakeImagesTerminal.py -p [-o]

    The terminal will prompt the user to insert lists of plots (operators as well if -o is used). Each plot and operator has unique settings that can be defined. Look at each plot and operator python file for specifics.

    To plot, the following format is used:
        [[<File>, <PlotType>, <Variable>, [Individual Options]] ...]

    Plotting example is shown below:
        [["dummy.vtk", "Pseudocolor", "TALLY_TAG", "Log", ('Min',0.00001), ('Max',0.0001)],["dummy.vtk", "Contour", "ERROR_TAG", "DASH"],["dummy.stl", "Mesh", "STL_mesh", "DASH"]]

    To add an operator, the following format is used:
        [[<Operator Type>, [Operator Options]] ...]

    Operators example is shown below:
        [{"Clip": {"oct": (1, 1, 1), "rot": (30, 30, 30), "loc":(0,0,0)}},
             ["Slice", ["y", 10]], [{"Clip": {"oct": (1, 1, 1)}}, ["Slice", ["x", 10]]],
             ["Threshold", ["Pseudocolor", "=", (5.14*10**-05,0.00011)]]]

2. Iterator.py can be imported in python and used as a class to do the same as Part 1.

3. Iterator.py can have the Vi.LaunchNowin() line commented. This allows for the script to be launched within the visit GUI using Controls -> Launch Cli. This combines Part 2 and the interactivity of the VisIt GUI.

----------------------------------------

If the same plotting settings are to be used on another data set containing similar spatial dimensions, XmlEdit.py can be used to replace loaded data in generated session files. This allows for application of exact operators, plots, and settings to another data set. The following is an example of use:

		python XmlEdit.py sample0.session dummy.stl dummy.vtk rmgrave.stl meshtal.vtk