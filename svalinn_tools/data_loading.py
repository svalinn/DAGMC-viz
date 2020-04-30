import argparse
import visit as Vi
from os import getcwd, path, system
from pymoab import core, tag, types


def parse_arguments():
    """
    Parse the argument list and return the location of a geometry file, the
    location of a data file, whether or not to save images with a timestamp of
    the four default plot windows and the VisIt session file in the current
    directory, and whether or not to open the session file in VisIt.

    Input:
    ______
       none

    Returns:
    ________
       args: Namespace
           User supplied geometry file location, data file location, and
           indication if the user wants images of the plot windows with a
           timestamp and the session file saved and opened in VisIt.
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
                        help="Indicate whether to save images of plot windows."
                        )
    parser.add_argument("-t", "--timestamp",
                        action="store_true",
                        help="Indicate whether to remove the timestamp from images."
                        )
    parser.add_argument("-s", "--sessionfile",
                        action="store_true",
                        help="Indicate whether to save the VisIt session file."
                        )
    parser.add_argument("-v", "--openvisit",
                        action="store_false",
                        help="Indicate whether to open the session file in VisIt."
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

    # Isolate the file name from string containing the file location.
    input_file = file_location.split("/")
    file_name = '.'.join(input_file[-1].split(".")[:-1])
    new_file_name = file_name + file_extension

    # Write the new file with the user supplied extension.
    mb.write_file(new_file_name)

    return new_file_name


def plane_slice_plotting(window_number, axis_number, label, images, timestamp):
    """
    Copy the Mesh, Pseudocolor, and Contour plots into a new VisIt window and
    slice through the proper axis.

    Input:
    ______
      window_number: int
          The number of the window to open (2,3, or 4).
      axis_number: int
          The number of the axis to slice through (0 for X, 1 for Y, 2 for Z).
      label: str
          The title of the plane slice.
      images: boolean
          Whether or not to save images of the plot windows.
      timestamp: boolean
          Whether or not to keep the timestamp on plot window images.

    Returns:
    ________
      none
    """

    # Open a new window with all three plots.
    Vi.AddWindow()
    Vi.CopyPlotsToWindow(1, window_number)

    # Create the plane slice plot by activating the mesh, pseudocolor, and contour plots.
    Vi.SetActiveWindow(window_number)
    Vi.SetActivePlots((0,1,2))

    # Remove the clip and slice operators from previous plot windows.
    Vi.RemoveAllOperators()

    # Add a slice through the proper axis.
    Vi.AddOperator("Slice", 1)
    s = Vi.SliceAttributes()
    s.axisType = axis_number
    Vi.SetOperatorOptions(s)

    # Include a label for each plane slice plot.
    banner = Vi.CreateAnnotationObject("Text2D")
    banner.position = (0.45, 0.92)
    banner.text = label
    banner.height = 0.05

    # Include the Svalinn logo in the bottom left corner of the plot.
    image = Vi.CreateAnnotationObject("Image")
    image.image = path.abspath(path.dirname(__file__)) + "/img/svalinn.png"
    image.position = (0.02, 0.02)
    image.width = 8
    image.height = 8

    Vi.DrawPlots()
    if images:
        if timestamp:
            attributes = Vi.GetAnnotationAttributes()
            attributes.userInfoFlag = 0
            Vi.SetAnnotationAttributes(attributes)
        Vi.SaveWindow()


def visit_config(geometry_file, data_file, args):
    """
    Convert geometry file to stl, convert data file to vtk, load each file
    into VisIt, and create and load a session file containing four plot windows.
        1) A cube with a slice through an octant.
        2) XY plane slice through the centroid.
        3) XZ plane slice through the centroid.
        4) YZ plane slice through the centroid.
    Each window has a mesh plot with the "STL_mesh" variable, a Pseudocolor plot
    with the "TALLY_TAG" variable, and the second, third, and fourth windows have
    Contour plots with the "ERROR_TAG" variable. If the user has indicated to,
    launch VisIt and load the session file.

    Input:
    ______
       geometry_file: h5m file
           User supplied geometry file.
       data_file: h5m or vtk file
           User supplied data file.
       args: Namespace
           User supplied geometry file location, data file location, and
           indication if the user wants images of the plot windows with a
           timestamp and the session file saved and opened in VisIt.

    Returns:
    ________
       None
    """

    # Create a list of dictionaries indicating the data, plot, and variable in VisIt.
    Files = [
        {"file_name" : data_file, "plot_type" : "Pseudocolor", "data_tag" : "TALLY_TAG"},
        {"file_name" : data_file, "plot_type" : "Contour", "data_tag" : "ERROR_TAG"},
        {"file_name" : geometry_file, "plot_type" : "Mesh", "data_tag" : "STL_mesh"}
    ]

    # Launch VisIt and add appropriate plots.
    Vi.LaunchNowin()
    for file in Files:
        Vi.OpenDatabase(file["file_name"])
        Vi.AddPlot(file["plot_type"],file["data_tag"])

    # Hide the contour plot in the first plot window.
    Vi.SetActivePlots(1)
    Vi.HideActivePlots()

    # Create the plot of the cube by activating the mesh and pseudocolor plots.
    Vi.SetActivePlots((0,2))

    # Set the view normal to the first octant.
    v = Vi.GetView3D()
    v.viewNormal = (1,1,1)
    Vi.SetView3D(v)

    # Apply a clip through the first octant.
    Vi.AddOperator("Clip")
    c = Vi.ClipAttributes()
    c.plane1Origin = (40,40,40)
    c.plane1Normal = (1,1,1)
    Vi.SetOperatorOptions(c)

    # Include the Svalinn logo in the bottom left corner of the plot.
    image = Vi.CreateAnnotationObject("Image")
    image.image = path.abspath(path.dirname(__file__)) + "/img/svalinn.png"
    image.position = (0.02, 0.02)
    image.width = 8
    image.height = 8

    Vi.DrawPlots()
    if args.images:
        if args.timestamp:
            attributes = Vi.GetAnnotationAttributes()
            attributes.userInfoFlag = 0
            Vi.SetAnnotationAttributes(attributes)
        Vi.SaveWindow()

    # Create the second plot of the XY plane slice.
    plane_slice_plotting(2, 2, "XY Plane", args.images, args.timestamp)

    # Create the third plot of the XZ plane slice.
    plane_slice_plotting(3, 1, "XZ Plane", args.images, args.timestamp)

    # Create the fourth plot of the YZ plane slice.
    plane_slice_plotting(4, 0, "ZY Plane", args.images, args.timestamp)

    # Display the four windows in a 2x2 grid.
    Vi.SetWindowLayout(4)

    # Save the session file with the default VisIt output to the current directory.
    visit_output = "VisitDefaultOutput.session"
    Vi.SaveSession(visit_output)
    Vi.Close()

    # Retrieve the path to the VisIt session file.
    session_file_path = path.join(getcwd(), visit_output)

    # If the user has indicated to, open the session file with the VisIt GUI.
    if args.openvisit:
        system("visit -sessionfile {} &".format(session_file_path))

    # If the user has indicated to, remove the session file after VisIt has opened.
    if not args.sessionfile:
        system("sleep 10; rm {}".format(session_file_path))


def main():

    args = parse_arguments()

    # Convert the geometry file and data file to the proper format.
    geometry_file = py_mb_convert(args.geofile, ".stl")
    data_file = py_mb_convert(args.datafile, ".vtk")

    # Create the VisIt session file and launch VisIt if the user has indicated to.
    visit_config(geometry_file, data_file, args)


if __name__ == "__main__":
    main()
