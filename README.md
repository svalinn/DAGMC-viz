# DAGMC-viz Documentation
The purpose of this toolkit is to assist with the visualization of DAGMC geometries in VisIt. This can include creating a default interactive view in VisIt, removing the graveyard volume from a given geometry, and expanding vector tags on a given mesh to facilitate database animation.

## Installation

The Direct Accelerated Geometry Monte Carlo visualization toolkit requires Python 2.7, VisIt 2.3.13 or above, and MOAB 5.1.0. The inclusion of VisIt and MOAB in the PYTHONPATH and the VisIt and MOAB executables in the PATH are required.The toolkit can be installed on a linux platform with the following command.

```
pip install svalinn-tools
```

If the user is in a Python environment, each of the three submodules can be accessed in the following way.

```
import svalinn_tools.{SUBMODULE}
```

## Description

### Data Loading 
This module can be used to create a default interactive output in VisIt from an h5m geometry file and an h5m or vtk data file. The following four interactive plot windows are displayed in a 2x2 grid.

      1. A cube with a clip through the first octant.
      2. XY plane slice through the centroid.
      3. XZ plane slice through the centroid.
      4. ZY plane slice through the centroid.

Each window has a mesh plot with the "STL_mesh" variable, a Pseudocolor plot with the "TALLY_TAG" variable, and the second, third, and fourth windows have Contour plots with the "ERROR_TAG" variable.

```
data_loading [geometryfile] [datafile]
```

The user may indicate whether or not they would like each window to be saved as a png file in their current directory by adding the ```-i``` option to the command. If the user would like to remove the timestamp from each image, the ```-t``` option can be added to the command as well.

```
data_loading [geometryfile] [datafile] -i -t
```

The user may indicate whether or not they would like the VisIt session file to be saved in their current directory by adding the ```-s``` option to the command. If the user does not want VisIt to be automatically launched, the ```-v``` option must be appended to the commmand as well.

```
data_loading [geometryfile] [datafile] -s -v
```

A sample output from an h5m geometry file and a vtk data file can be seen below.

![alt text](https://raw.githubusercontent.com/piperlincoln/DAGMC-viz/add-setup-script/svalinn_tools/img/README_example.png)

----------------------------------------

### Graveyard Removal
This module can be used to remove the graveyard volume/group from an h5m geometry file. The new file will be written in the current directory with ```_no_grave.h5m``` appended to the original file name. It can also extract curve, surface, and volume EntitySets.

```
graveyard_removal [h5mfile]
```

The user may specify a specific output file name and extension by adding the ```-o``` option to the command. The new file will be written in the current directory. The user may also specify if they would like the entity handle of the graveyard volume/group to be printed by adding the ```-p``` option to the command.

```
graveyard_removal [h5mfile] -o [outputfile] -p
```

----------------------------------------

### Tag Expansion 
This module can be used to expand vector tags on a mesh and generate a data file for each value in the vector tag. VisIt will recognize the collection of these data files as a database, and permit stepping through them in an animation.

```
tag_expansion [meshfile]
```

The user may specify a directory name by adding the ```-d``` option to the command. If the user would like a previous directory to be overwritten, the ```-o``` option may be specified as well. If the user would like the vector tags on a specific element in the mesh to be expanded, the ```-e``` option may also be used.

```
tag_expansion -e [element] -d [directory] -o
```
----------------------------------------

NOTE: This is based on [previous work](https://github.com/piperlincoln/DAGMC-viz/tree/lane-progress) done by Lane Schultz.
