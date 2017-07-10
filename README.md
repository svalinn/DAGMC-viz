Outdated Documentation


DAGMC-viz Documentation
=======================

(Note: Python 2.7 and visit are required. Python path needs to be set for visit. Default operators rely on Pseudocolor for spatial definition.)

1. MakeImagesTerminal.py can be used to load data.
	
		python MakeImagesTerminal.py -i

    The terminal will prompt the user to insert lists of plots. Operators may also be added. Each plot and operator has unique settings that can be defined. Look at each plot and operator python file for specifics.

    To plot, the following format is used:

        [[<File>, <PlotType>, <Variable>, [Individual Options]] ...]

    Plotting example is shown below:

        [
        ["dummy.vtk", "Pseudocolor", "TALLY_TAG", "Log", ('Min',0.00001),('Max',0.0001)],
        ["dummy.vtk", "Contour", "ERROR_TAG", "DASH"],
        ["dummy.stl", "Mesh", "STL_mesh", "DASH"]
        ]

    To add an operator, the following format is used:

        [[<Operator Type>, [Operator Options]] ...]

    Operators example is shown below:

        [
        {"Clip": {"oct": (1, 1, 1), "rot": (30, 30, 30), "loc":(0,0,0)}},
             ["Slice", ["y", 10]], [{"Clip": {"oct": (1, 1, 1)}}, ["Slice", ["x", 10]]],
             ["Threshold", ["Pseudocolor", "=", (5.14*10**-05,0.00011)]]
        ]

2. MakeImagesTerminal.py has an option to display tally data, error associated with tally data, three slices (x/y/z) at the origin, and a clip of the first octant by default. The session file associated with this option can be loaded in VisIt to view all options with the same orientation.
    
        python MakeImagesTerminal.py -d

3. Multiple windows with other options of operators can be viewed. A maximum of 16 windows are supported by VisIt. The following with an input of plot lists and operator lists can be used:

        python MakeImagesTerminal.py -w

4. Multiple axis can be inserted without delimiters for automatic slicing. The number of slices across each axis can be defined. Slices are programmed to be evenly distributed between maximum and minimum spatial dimensions of Pseudocolor plots. The first two are of the maximum and minimum spatial dimensions. More than two slices are needed for this option to work. To invoke this function the following can be used:

        python MakeImagesTerminal.py -m

5. Multiple orbital views can be gathered horizontally, vertically, or both. The number of images for each orbit can be defined. The larger the number of images the "smoother" an animation would be from collected images. 

        python MakeImagesTerminal.py -o



----------------------------------------

If the same plotting settings are to be used on another data set containing similar spatial dimensions, XmlEdit.py can be used to replace loaded data in generated session files. This allows for application of exact operators, plots, and settings to another data set. The following is an example of use:

		python XmlEdit.py sample0.session dummy.stl dummy.vtk rmgrave.stl meshtal.vtk


----------------------------------------

Bash option coming in the future.