DAGMC-viz Documentation
=======================

Note: Python 2.7, VisIt, and MOAB are required. The Python path should be set for VisIt and MOAB. This branch is based on previous work done by Lane Schultz, which can be viewed in the "lane_progress" branch of the repository. Functionality allowing the user to completely determine the VisIt output is on the way.

----------------------------------------

1. DataLoading.py can be used to create a default output in VisIt from an h5m geometry file and an h5m or vtk data file. The following four interactive plot windows are displayed in a 2x2 grid.

       1) A cube with a slice through an octant in order to see the center.
       2) XY plane slice through the center.
       3) XZ plane slice through the center.
       4) YZ plane slice through the center.
Each window has a mesh plot with the "STL_mesh" variable, a Pseudocolor plot with the "TALLY_TAG" variable, and the second, third, and fourth windows have Contour plots with the "ERROR_TAG" variable. The user may indicate whether or not they would like each window to be saved as a png file in their current directory.

       python DataLoading.py [geometry_file] [data_file] -i 

----------------------------------------

2. GraveIdentifyAndRemove.py can be used to remove the graveyard EntitySet from an h5m geometry file. The user may specify a specific output file name and extension. It can also extract curve, surface, and volume EntitySets.
 
        python GraveIdentifyAndRemove.py [h5m file] -o [output file] 
		
----------------------------------------

Bash scripts for converting a file to another format and substituting loaded datasets into VisIt are under /BashTool.

----------------------------------------
