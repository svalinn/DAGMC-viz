DAGMC-viz Documentation
=======================

Note: Python 2.7, ViSit, and MOAB are required.
Python path should be set for VisIt and MOAB.
Lane's work can be viewed in the lane_progress branch of this repository.
Functionality allowing the user to completely determine the VisIt output is on the way.

----------------------------------------

1. DataLoading.py can be used to create a default output in VisIt from a geometry file and a data file. A 3D plot and three 2D plane slices are displayed in an interactive 2x2 grid. The user may indicate whether or not they would like each window to be saved as a png file in their current directory.
	
		python DataLoading.py [geometry_file] [data_file] -i 

----------------------------------------

2. GraveIdentifyAndRemove.py can be used to remove the graveyard EntitySet from an h5m geometry file. The user may specify a specific output file name and extension. It can also extract curve, surface, and volume EntitySets.
 
        python GraveIdentifyAndRemove.py [h5m file] -o [output file] 
		
----------------------------------------

Bash scripts for converting a file to another format and substituting loaded datasets into VisIt are under /BashTool.

----------------------------------------
