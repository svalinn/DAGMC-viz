DAGMC-viz Documentation
=======================

Note: Python 2.7 and visit are required.
Python path needs to be set for visit.
Default operators rely on Pseudocolor for spatial definition.
mbconvert and mbgsets are used for bash options.

----------------------------------------

1. MakeImagesTerminal.py can be used to load data.
	
		python MakeImagesTerminal.py -pl [plot list] -op [operator list]

    The terminal will prompt the user to insert lists of plots. Operators may also be added. Each plot and operator has unique settings that can be defined. Look at each plot and operator python file for specifics.

    To plot, the following format is used:

        [[<File>, <PlotType>, <Variable>, [Individual Options]] ...]

    Plotting example is shown below:

        [['test.vtk', 'Pseudocolor', 'TALLY_TAG', 'Log', ('Min',0.00001),('Max',0.0001)],['test.vtk', 'Contour', 'ERROR_TAG', 'DASH'],['test.stl', 'Mesh', 'STL_mesh', 'DASH']]

    To add an operator, the following format is used:

        [[<Operator Type>, [Operator Options]] ...]

    Operators example is shown below:

        [{'Clip': {'oct': (1, 1, 1), 'rot': (30, 30, 30), 'loc':(0,0,0)}},['Slice', ['y', 10]], [{'Clip': {'oct': (1, 1, 1)}}, ['Slice', ['x', 10]]],['Threshold', ['Pseudocolor', '=', '(5.14*10**-05,0.00011)']]]

    Gathering multiple images and session files can be done with the -im options as follows:

        python MakeImagesTerminal.py -pl [plot list] -op [operator list] -im

        python MakeImagesTerminal.py -pl "[['test.vtk','Pseudocolor','TALLY_TAG','Log',('Min',0.00001),('Max',0.0001)], ['test.vtk','Contour','ERROR_TAG','DASH'],]" -op "[{'Clip': {'oct': (1, 1, 1), 'rot': (30, 30, 30), 'loc':(0,0,0)}},['Slice', ['y', 10]], [{'Clip': {'oct': (1, 1, 1)}}, ['Slice', ['x', 10]]],['Threshold', ['Pseudocolor', '=', '(5.14*10**-05,0.00011)']]]" -im


2. MakeImagesTerminal.py has an option to display tally data, error associated with tally data, three slices (x/y/z) at the origin, and a clip of the first octant by default. The session file associated with this option can be loaded in VisIt to view all options with the same orientation.
    
        python MakeImagesTerminal.py -pl [plot list] -de

        python MakeImagesTerminal.py -pl "[['test.vtk','Pseudocolor','TALLY_TAG','Log',('Min',0.00001),('Max',0.0001)], ['test.vtk','Contour','ERROR_TAG','DASH'],]" -de

3. Multiple windows with other options of operators can be viewed. A maximum of 16 windows are supported by VisIt. The following with an input of plot lists and operator lists can be used:

        python MakeImagesTerminal.py -pl [plot list] -op [operator list] -wi

        python MakeImagesTerminal.py -pl "[['test.vtk','Pseudocolor','TALLY_TAG','Log',('Min',0.00001),('Max',0.0001)], ['test.vtk','Contour','ERROR_TAG','DASH'],]" -op "[{'Clip': {'oct': (1, 1, 1)}},{'Clip': {'oct': (-1, 1, 1)}},[{'Clip': {'oct': (1, 1, 1)}}, ['Slice', ['x', 10]]]]" -wi


4. Multiple axis can be inserted without delimiters for automatic slicing. The number of slices across each axis can be defined. Slices are programmed to be evenly distributed between maximum and minimum spatial dimensions of Pseudocolor plots. The first two are of the maximum and minimum spatial dimensions. More than two slices are needed for this option to work. To invoke this function the following can be used:

        python MakeImagesTerminal.py -pl [plot list] -mu [axes, number of slices]

        python MakeImagesTerminal.py -pl "[['test.vtk','Pseudocolor','TALLY_TAG','Log',('Min',0.00001),('Max',0.0001)], ['test.vtk','Contour','ERROR_TAG','DASH'],]" -op "[[{'Clip': {'oct': (1, 1, 1)}},{'Clip': {'oct': (-1, 1, 1)}}]]" -mu "['xyz',2]"


5. Multiple orbital views can be gathered horizontally, vertically, or both. The number of images for each orbit can be defined. The larger the number of images the "smoother" an animation would be from collected images. 

        python MakeImagesTerminal.py -pl [plot list] -op [operator list] -or "['yes','view',number of views]"

        python MakeImagesTerminal.py -pl "[['test.vtk','Pseudocolor','TALLY_TAG','Log',('Min',0.00001),('Max',0.0001)], ['test.vtk','Contour','ERROR_TAG','DASH'],]" -op "[{'Clip': {'oct': (1, 1, 1)}},{'Clip': {'oct': (-1, 1, 1)}}]" -or "['both',20]"


----------------------------------------

Bash scripts for removing a graveyard from an h5m file, extracting surfaces, extracting, curves, and substituting loaded datasets are under /BashTool.

To convert an h5m file to stl or a meshtal file to vtk, the following examples can be used:

        python MakeImagesTerminal.py -d1 "['meshtal','test.vtk']"
        python MakeImagesTerminal.py -d2 "['fng_zip.h5m','test.stl']"  

To remove a graveyard, the following example can be used:

        python MakeImagesTerminal.py -gr "['fng_zip.h5m','rmgrave.stl']"

To extract surfaces, the following example can be used:

        python MakeImagesTerminal.py -su "['fng_zip.h5m','test.stl']"

To extract curves, the following example can be used:

        python MakeImagesTerminal.py -cu "['fng_zip.h5m','test.vtk']"

To replace data to be loaded in a single session file, the following example can be used:

        python MakeImagesTerminal.py -se "['sample0.session','test.stl','rmgrave.stl']"

To replace data to be loaded in all session files under the original session file directory, the following example can be used:

        python MakeImagesTerminal.py -sm "['test.stl','rmgrave.stl']"

Images from edited session files can be gathered by running the following:

        python MakeImagesTerminal.py -gi 

----------------------------------------

Bash options can be used in conjunction with python scripts to remove a graveyard, load data, replace the loaded data, and get images from replaced loaded data file. An example is shown below.

        python MakeImagesTerminal.py -d1 "['fng_zip.h5m','test.stl']" -d2 "['meshtal','test.vtk']" -pl "[['test.vtk','Pseudocolor','TALLY_TAG','Log',('Min',0.00001),('Max',0.0001)], ['test.vtk','Contour','ERROR_TAG','DASH'], ['test.stl','Mesh','STL_mesh']]" -op "[{'Clip': {'oct': (1, 1, 1), 'rot': (30, 30, 30), 'loc':(0,0,0)}},['Slice', ['y', 10]], [{'Clip': {'oct': (1, 1, 1)}}, ['Slice', ['x', 10]]],['Threshold', ['Pseudocolor', '=', '(5.14*10**-05,0.00011)']]]" -im -gr "['fng_zip.h5m','rmgrave.stl']" -sm "['test.stl','rmgrave.stl']" -gi
