DAGMC-viz Documentation
=======================

The Direct Accelerated Geometry Monte Carlo visualization toolkit requires Python 2.7, VisIt 2.3.13, and MOAB 5.1.0. The inclusion of VisIt and MOAB in the PYTHONPATH and the VisIt and MOAB executables in the PATH are required.

----------------------------------------

1. data_loading.py can be used to create a default interactive output in VisIt from an h5m geometry file and an h5m or vtk data file. The following four interactive plot windows are displayed in a 2x2 grid.

      1. A cube with a clip through the first octant.
      2. XY plane slice through the centroid.
      3. XZ plane slice through the centroid.
      4. ZY plane slice through the centroid.

Each window has a mesh plot with the "STL_mesh" variable, a Pseudocolor plot with the "TALLY_TAG" variable, and the second, third, and fourth windows have Contour plots with the "ERROR_TAG" variable.

```
python data_loading.py [geometryfile] [datafile]
```
The user may indicate whether or not they would like each window to be saved as a png file in their current directory by adding the ```-i``` option to the command. If the user would like to remove the timestamp from each image, the ```-t``` option can be added to the command as well.

```
python data_loading.py [geometryfile] [datafile] -i -t
```
The user may indicate whether or not they would like the VisIt session file to be saved in their current directory by adding the ```-s``` option to the command. If the user does not want VisIt to be automatically launched, the ```-v``` option must be appended to the commmand as well.

```
python data_loading.py [geometryfile] [datafile] -s -v
```

A sample output from an h5m geometry file and a vtk data file can be seen below.

![alt text](https://github.com/piperlincoln/DAGMC-viz/blob/add-setup-script/img/README_example.png)

----------------------------------------

2. graveyad_removal.py can be used to remove the graveyard volume/group from an h5m geometry file. The new file will be written in the current directory with ```_no_grave.h5m``` appended to the original file name. It can also extract curve, surface, and volume EntitySets.

```
python graveyard_removal.py [h5mfile]
```

The user may specify a specific output file name and extension by adding the ```-o``` option to the command. The new file will be written in the current directory. The user may also specify if they would like the entity handle of the graveyard volume/group to be printed by adding the ```-p``` option to the command.

```
python graveyard_removal.py [h5mfile] -o [outputfile] -p
```

----------------------------------------

3. TagExpansion.py can be used to expand vector tags on a mesh and generate a data file for each value in the vector tag. VisIt will recognize the collection of these data files as a database, and permit stepping through them in an animation.

```
python tag_expansion.py [meshfile]
```

The user may specify a directory name by adding the ```-d``` option to the command. If the user would like a previous directory to be overwritten, the ```-o``` option may be specified as well. If the user would like the vector tags on a specific element in the mesh to be expanded, the ```-e``` option may also be used.

```
python tag_expansion.py -e [element] -d [directory] -o
```
----------------------------------------

NOTE: This is based on [previous work](https://github.com/piperlincoln/DAGMC-viz/tree/lane-progress) done by Lane Schultz.
