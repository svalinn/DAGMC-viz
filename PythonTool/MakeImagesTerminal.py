import argparse
import timeit
import ast

from GrabImagesFromSessions import GrabImagesFromSessions
from BashOptions import BashOptions

tic = timeit.default_timer()  # Start timer.

# The following are help message descriptions for each argument.

helpdataconvert1 = (
    """This action calls mbconvert via the tool.

    An example input is as follows:

    -ds "['fng_zip.h5m','test.stl']"
    """
    )

helpdataconvert2 = (
    """This action calls mbconvert via the tool.

    An example input is as follows:

    -dv "['meshtal','test.vtk']"
    """
    )

helpgraveremove = (
    """Remove graveyard from mesh.
    Bash file GraveRemove.sh finds and removes
    graveyard geometry.

    An example input is as follows:

    -gr "['fng_zip.h5m','rmgrave.stl']"
    """
    )

helpsurfaces = (
    """Create surface file from h5m file.
    Bash file Surfaces.sh used to extract surfaces

    An example input is as follows:

    -su "['fng_zip.h5m','test.stl']"
    """
    )

helpcurves = (
    """Create curve file from h5m file.
    Bash file Curves.sh used to extract curves

    An example input is as follows:

    -cu "['fng_zip.h5m','test.stl']"
    """
    )

helpplots = (
    """List of plots.

    An example input is as follows:

    -pl "[['test.vtk','Pseudocolor','TALLY_TAG',
    'Log',('Min',0.00001),('Max',0.0001)],
    ['test.vtk','Contour','ERROR_TAG','DASH'],
    ['test.stl','Mesh','STL_mesh']]" """
    )

helpoperators = (
    """List of operators.

    An example input is as follows:

    -op "[{'Clip': {'oct': (1, 1, 1), 'rot': (30, 30, 30), 'loc':(0,0,0)}},
    ['Slice', ['y', 10]],
    [{'Clip': {'oct': (1, 1, 1)}},['Slice', ['x', 10]]],
    ['Threshold', ['Pseudocolor', '=', '(5.14*10**-05,0.00011)']]]"
    """
    )

helpimages = (
    """Make images of plots and operators.
    Once plots and/or operators are defined,
    images and session files are gathered
    with this option. If no operators are defined,
    an image of the plots will be attained.
    If operators are defined, then images and sessions
    will be generated for each list of operators.

    An example input is as follows:

    -im
    """
    )

helpwindows = (
    """Open multiple windows.
    Multiple windows with loaded plots and applied
    operators (if defined) will be displayed on individual windows.
    Each window has locked views. A maximum of 16 windows can be used.

    An example input is as follows:

    -wi
    """
    )

helpdefault = (
    """Apply default operators.
    This opens windows containing the following:
    Windows with each plot defined without operators.
    Slices in x, y, and z at the centroid of a pseudocolor plot.
    A clip in the first octant at the centroid of a pseudocolor plot.

    An example input is as follows:

    -de
    """
    )

helpmultislice = (
    """Apply only slices.
    This function evenly distributes slices along defined axis.
    The number of slices must be greater than 1.

    An example input is as follows:

    -mu "['xyz',20]"
    """
    )

helporbit = (
    """Gather orbital view (vertical/horizontal/both).
    Take multiple views around vertically, horizontally, or both.
    Views are evenly spaced.
    OrbitOptions = (<axis>, <number of views>).

    The higher the number of views the smoother the rotation.

    This assumes the following positive axis orientation:
    y - Up
    x - Right
    z - Out from screen

    An example input is as follows:

    -or "['both',20]"
    """
    )

helpsessionreplacesingle = (
    """Replace loaded data from a session file.

    An example input is as follows:

    -se "['sample0.session','test.stl','rmgrave.stl']"
    """
    )

helpsessionreplacemultiple = (
    """Replace loaded data of all session files.

    An example input is as follows:

    -sm "['test.stl','rmgrave.stl']"
    """
    )

helpgrabimagesfromsessions = (
    """Load sessions and grab window images.

    An example input is as follows:

    -gi
    """
    )

parser = argparse.ArgumentParser(description="Terminal execution of tool.",
                                 usage="Create plots to save.",
                                 formatter_class=argparse.RawTextHelpFormatter,
                                 )

parser.add_argument("-d1", "--dataconvert1",
                    type=str,
                    help=helpdataconvert1,
                    )
parser.add_argument("-d2", "--dataconvert2",
                    type=str,
                    help=helpdataconvert2,
                    )
parser.add_argument("-gr", "--graveremove",
                    type=str,
                    help=helpgraveremove,
                    )
parser.add_argument("-su", "--surfacesnograve",
                    type=str,
                    help=helpsurfaces,
                    )
parser.add_argument("-cu", "--curvesnograve",
                    type=str,
                    help=helpcurves,
                    )
parser.add_argument("-pl", "--plots",
                    type=str,
                    help=helpplots,
                    )
parser.add_argument("-op", "--operators",
                    type=str,
                    help=helpoperators,
                    )
parser.add_argument("-im", "--images",
                    action="store_true",
                    help=helpimages,
                    )
parser.add_argument("-wi", "--windows",
                    action="store_true",
                    help=helpwindows,
                    )
parser.add_argument("-de", "--default",
                    action="store_true",
                    help=helpdefault,
                    )
parser.add_argument("-mu", "--multislice",
                    type=str,
                    help=helpmultislice,
                    )
parser.add_argument("-or", "--orbit",
                    type=str,
                    help=helporbit,
                    )
parser.add_argument("-se", "--sessionreplacesingle",
                    type=str,
                    help=helpsessionreplacesingle,
                    )
parser.add_argument("-sm", "--sessionreplacemultiple",
                    type=str,
                    help=helpsessionreplacemultiple,
                    )
parser.add_argument("-gi", "--grabimagesfromsessions",
                    action="store_true",
                    help=helpgrabimagesfromsessions,
                    )

args = parser.parse_args()

# Gather plot and operator inputs.
if args.plots:
    # Imported here to avoid loading the viewer when not needed.
    from VisitOptions import VisitOptions
    FilePlots = ast.literal_eval(args.plots)

    if args.operators:
        OperatorSet = ast.literal_eval(args.operators)
        Options = VisitOptions(args, FilePlots, OperatorSet)
    else:
        Options = VisitOptions(args, FilePlots)

if args.dataconvert1:
    BashCommand = args.dataconvert1
    FileBash = BashOptions(BashCommand)
    FileBash.DataConvert()

if args.dataconvert2:
    BashCommand = args.dataconvert2
    FileBash = BashOptions(BashCommand)
    FileBash.DataConvert()

if args.graveremove:
    BashCommand = args.graveremove
    FileBash = BashOptions(BashCommand)
    FileBash.GraveRemove()

if args.surfacesnograve:
    BashCommand = args.surfacesnograve
    FileBash = BashOptions(BashCommand)
    FileBash.SurfacesNoGrave()

if args.curvesnograve:
    BashCommand = args.curvesnograve
    FileBash = BashOptions(BashCommand)
    FileBash.CurvesNoGrave()

if args.images:
    Options.Images()

if args.windows:
    Options.Windows()

if args.default:
    Options.Default()

if args.multislice:
    Options.MultiSlice()

if args.orbit:
    Options.Orbit()

if args.sessionreplacesingle:
    BashCommand = args.sessionreplacesingle
    FileBash = BashOptions(BashCommand)
    FileBash.SessionReplaceSingle()

if args.sessionreplacemultiple:
    BashCommand = args.sessionreplacemultiple
    FileBash = BashOptions(BashCommand)
    FileBash.SessionReplaceMultiple()

if args.grabimagesfromsessions:
    GrabImagesFromSessions()

toc = timeit.default_timer()  # End timer.
ElapsedTime = toc - tic
print "Elapsed time was " +str(ElapsedTime)+ " seconds."
