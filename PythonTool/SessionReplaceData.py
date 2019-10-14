import argparse
import os
import visit as Vi
from DataLoading import py_mb_convert
from pymoab import core, tag, types


def parse_arguments():
    """
    Parse the argument list and return the location of a session file, a new
    geometry file, a new data file, and the name of the new session file.
    Input:
    ______
       none
    Returns:
    ________
       args: Namespace
           User supplied session file, geometry file, and data file location,
           and name of new session file.
    """

    parser = argparse.ArgumentParser(description="Replace data in session file.")

    parser.add_argument("sessionfile",
                        type=str,
                        help="Provide a path to the session file."
                        )
    parser.add_argument("-g", "--geofile",
                        type=str,
                        help="Provide a path to the geometry file."
                        )
    parser.add_argument("-d", "--datafile",
                        type=str,
                        help="Provide a path to the data file."
                        )
    parser.add_argument("-o", "--outputfile",
                        type=str,
                        help="Provide a name for the new session file."
                        )

    args = parser.parse_args()

    return args


def replace_session_data(session_file, geometry_file = None, data_file = None, output_file = None):
    """
    Convert geometry file to stl, convert data file to vtk, replace the data
    in the session file, and open VisIt with the updated session file.
    Input:
    ______
       session_file: VisIt file
           User supplied VisIt session file.
       geometry_file: h5m file
           User supplied file containing geometry of interest.
       data_file: h5m or vtk file
           User supplied file containing data of interest.
       output_file: str
           User supplied name of the new session file.
    Returns:
    ________
       none
    """

    if geometry_file is None and data_file is None:
        print("WARNING: No new geometry or data file provided.")
        exit()

    if geometry_file is not None:
        # Convert the geometry file to the proper format.
        geometry_file = py_mb_convert(geometry_file, ".stl")

    if data_file is not None:
        # Convert the data file to the proper format.
        data_file = py_mb_convert(data_file, ".vtk")

    # Restore the session file in VisIt and replace the geometry and/or data file.
    Vi.LaunchNowin()
    Vi.RestoreSession(session_file, 0)
    Vi.ReplaceDatabase(geometry_file)

    # Create the new session file.
    if output_file is None:
        Vi.SaveSession(session_file)
    else:
        Vi.SaveSession(output_file)
    Vi.Close()

    # Open the VisIt GUI with the new session file.


def main():

  # Parse arguments.
  args = parse_arguments()

  # Replace the data in the session file with what the user supplied.
  replace_session_data(args.sessionfile, args.geofile, args.datafile, args.outputfile)


if __name__ == "__main__":
  main()
