Outdated Documentation


DAGMC-viz Documentation
=======================

(Note: Python 2.7 and visit are required.)

There are three primary methods of use for this tool.

1. MakeImagesTerminal.py can be used to load data with plot and variable names in Inputs.py. The following is an example input that loads data (-pl), applies an operator (-op), applies plot and operator settings (-se), and then saves images and session files (-sa).:
	
		python MakeImagesTerminal.py -pl -op -se -sa

2. MakeImagesPython.py can be imported in python and used as a class to do the same as Part 1.

3. MakeImagesPython.py can have the Vi.LaunchNowin() line commented. This allows for the script to be launched within the visit GUI using Controls -> Launch Cli. This combines Part 2 and the interactivity of the VisIt GUI.

----------------------------------------

If the same plotting settings are to be used on another data set containing similar spatial dimensions, XmlEdit.py can be used to replace loaded data in generated session files. This allows for application of exact operators, plots, and settings to another data set. The following is an example of use:

		python XmlEdit.py sample0.session rmgrave.stl meshtal.vtk

For this to work, the original stl and vtk files need to be called dummy.stl and dummy.vtk respectively. This example replaces dummy files in sample0.session with rmgrave.stl and meshtal.vtk.