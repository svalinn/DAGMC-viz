import argparse
import os
import visit as Vi
from GraveIdentifyAndRemove import remove_graveyard
from pymoab import core, types, tag


def parse_arguments():
    """
    Parse the argument list and return the location of a geometry file, the
    location of a data file, and indication if the user wants images of the
    four default plot windows saved or not in the current directory.

    Input:
    ______
       none

    Returns:
    ________
       args: Namespace
           User supplied geometry file location, data file location, and
           indication if the user wants images of the plot windows saved.
    """

    parser = argparse.ArgumentParser(description="Create default VisIt output.")

    parser.add_argument("geofile",
                        type=str,
                        help="Provide a path to the geometry file."
                        )
    parser.add_argument("datafile",
                        type=str,
                        help="Provide a path to the data file."
                        )

    parser.add_argument("-i", "--images",
                        action="store_true",
                        help="Indicate whether or not to save images of plot windows."
                        )

    args = parser.parse_args()

    return args


def py_mb_convert(file_location, file_extension):
   """
   Convert files from one format to another with PyMOAB.

   Input:
   ______
      file_location: str
          User supplied file location.
      file_extension: str
          User supplied file format to convert to, including '.'

   Returns:
   ________
      new_file_name: str
          The new file name with the specified extension.
   """

   # Load the file to be converted.
   mb = core.Core()
   mb.load_file(file_location)

   # Isolate file name from string containing the file location.
   input_array = file_location.split("/")
   input_file = input_array[-1]
   base_file_name = input_file[:-4]
   new_file_name = base_file_name + file_extension

   # Write the new file with the user supplied extension.
   mb.write_file(new_file_name)

   return new_file_name


def plane_slice_plotting(window_number, axis_number, label, images):
    """
    Copy the Mesh, Pseudocolor, and Contour plots into a new VisIt window and
    slice through the proper axis.

    Input:
    ______
      window_number: int
          The number of the window to open (2,3, or 4).
      axis_number: int
          The number of the axis to slice through (0 for X, 1 for Y, 2 for Z).
      images: boolean
          Whether or not to save images of the plot windows.

    Returns:
    ________
      none
    """

    # Open a new window with all three plots active.
    Vi.AddWindow()
    Vi.CopyPlotsToWindow(1, window_number)

    # Create the plane slice plot by activating the mesh, pseudocolor, and contour plots.
    Vi.SetActivePlots((0,1,2))

    # Add a slice through the proper axis.
    Vi.AddOperator("Slice", 1)
    s = Vi.SliceAttributes()
    s.axisType = axis_number
    Vi.SetOperatorOptions(s)

    banner = Vi.CreateAnnotationObject("Text2D")
    banner.position = (0.45, 0.92)
    banner.text = label
    banner.height = 0.05

    Vi.DrawPlots()
    if images:
        Vi.SaveWindow()


def data_loading(geometry_file, data_file, images):
   """
   Convert geometry file to stl, convert data file to vtk, load each file
   into VisIt, and create and load a session file containing the four plot windows.
       1) A cube with a slice through an octant in order to see the center.
       2) XY plane slice through the center.
       3) XZ plane slice through the center.
       4) YZ plane slice through the center.
   Each window has a mesh plot with the "STL_mesh" variable, a Pseudocolor plot
   with the "TALLY_TAG" variable, and the second, third, and fourth windows have
   Contour plots with the "ERROR_TAG" variable.

   Input:
   ______
      geometry_file: h5m file
          User supplied file containing geometry of interest.
      data_file: h5m or vtk file
          User supplied file containing data of interest.
      images: boolean
          Whether or not to save images of the plot windows.

   Returns:
   ________
      none
   """

   # Remove the graveyard from the geometry file.
   geometry_file = remove_graveyard(geometry_file)

   # Convert the geometry file and data file to the proper format.
   geometry_file = py_mb_convert(geometry_file, ".stl")
   data_file = py_mb_convert(data_file, ".vtk")

   # Create a list of dictionaries indicating the data, plot, and variable in VisIt.
   Files = [
       {"file_name" : geometry_file, "plot_type" : "Mesh", "data_tag" : "STL_mesh"},
       {"file_name" : data_file, "plot_type" : "Pseudocolor", "data_tag" : "TALLY_TAG"},
       {"file_name" : data_file, "plot_type" : "Contour", "data_tag" : "ERROR_TAG"}
       ]

   Vi.LaunchNowin()
   for file in Files:
       Vi.OpenDatabase(file["file_name"])
       Vi.AddPlot(file["plot_type"],file["data_tag"])

   # Create the first plot of the cube by activating the mesh and pseudocolor plots.
   Vi.SetActivePlots((0,1))

   # Set the view normal to the first octant.
   v = Vi.GetView3D()
   v.viewNormal = (1,1,1)
   Vi.SetView3D(v)

   Vi.DrawPlots()
   if images:
       Vi.SaveWindow()

   # Create the second plot of the XY plane slice.
   plane_slice_plotting(2, 2, "XY Plane", images)

   # Create the third plot of the XZ plane slice.
   plane_slice_plotting(3, 1, "XZ Plane", images)

   # Create the fourth plot of the YZ plane slice.
   plane_slice_plotting(4, 0, "ZY Plane", images)

   # Display the four windows in a 2x2 grid.
   Vi.SetWindowLayout(4)

   # Save the session file with the default VisIt output to the current directory.
   visitOutput = "visitOutput.session"
   Vi.SaveSession(visitOutput)
   Vi.Close()

   # Determine the absolute path to the session file and open it with the VisIt GUI.
   curDir = os.getcwd()
   os.system("visit -sessionfile {} &".format(curDir + "/" + visitOutput))


def main():

  # Parse arguments.
  args = parse_arguments()

  # Create the default VisIt output.
  data_loading(args.geofile, args.datafile, args.images)


if __name__ == "__main__":
  main()
