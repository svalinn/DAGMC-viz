DAGMC-viz Documentation
=======================

The Direct Accelerated Geometry Monte Carlo visualization toolkit requires Python 2.7, VisIt, and MOAB. The inclusion of VisIt and MOAB in the PYTHONPATH and the VisIt executable in the PATH is required. A user can input a geometry file and a data file to produce default interactive output in VisIt, with the option to save images of the plot windows as well. Functionality allowing the user to have full control of determining the output will be implemented in the future.

----------------------------------------

1. DataLoading.py can be used to create a default output in VisIt from an h5m geometry file and an h5m or vtk data file. The following four interactive plot windows are displayed in a 2x2 grid.

      1. A cube with the default view normal to a corner.
      2. XY plane slice through the center.
      3. XZ plane slice through the center.
      4. ZY plane slice through the center.
      
Each window has a mesh plot with the "STL_mesh" variable, a Pseudocolor plot with the "TALLY_TAG" variable, and the second, third, and fourth windows have Contour plots with the "ERROR_TAG" variable. 

```
python DataLoading.py [geometry_file] [data_file] 
```
The user may indicate whether or not they would like each window to be saved as a png file in their current directory by adding the ```-i``` option to the command.

```
python DataLoading.py [geometry_file] [data_file] -i 
```

A sample output from an h5m geometry file and a vtk data file can be seen below.

<p align="center">
<img src="https://i.postimg.cc/Fzb5jM6t/Screenshot-from-2018-11-02-13-37-55.png" width="400" height="400"/>
</p>

----------------------------------------

2. GraveIdentifyAndRemove.py can be used to remove the graveyard volume/group from an h5m geometry file. The user may specify a specific output file name and extension. It can also extract curve, surface, and volume EntitySets.
 
```
python GraveIdentifyAndRemove.py [h5m file] -o [output file] 
```

----------------------------------------

Bash scripts for converting a file to another format and substituting loaded datasets into VisIt are under /BashTool.

----------------------------------------

NOTE: This is based on [previous work](https://github.com/piperlincoln/DAGMC-viz/tree/lane_progress) done by Lane Schultz.
