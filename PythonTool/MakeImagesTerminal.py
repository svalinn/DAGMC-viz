import argparse
import timeit
import ast

from GrabImagesFromSessions import GrabImagesFromSessions
from BashOptions import BashOptions

tic = timeit.default_timer()  # Start timer.

parser = argparse.ArgumentParser(description="Terminal execution of tool.",
                                 usage="Create plots to save.",
                                 )

parser.add_argument("-ds", "--dataconvertstl",
                    type=str,
                    help="Convert h5m to stl.",
                    )
parser.add_argument("-dv", "--dataconvertvtk",
                    type=str,
                    help="Convert h5m to vtk.",
                    )
parser.add_argument("-gr", "--graveremove",
                    type=str,
                    help="Remove grave yard from mesh.",
                    )
parser.add_argument("-su", "--surfaces",
                    type=str,
                    help="Create curve file from h5m file.",
                    )
parser.add_argument("-cu", "--curves",
                    type=str,
                    help="Create curve file from h5m file.",
                    )
parser.add_argument("-pl", "--plots",
                    type=str,
                    help="List of plots.",
                    )
parser.add_argument("-op", "--operators",
                    type=str,
                    help="List of operators.",
                    )
parser.add_argument("-im", "--images",
                    action="store_true",
                    help="Make images of plots and operators.",
                    )
parser.add_argument("-wi", "--windows",
                    action="store_true",
                    help="Open multiple windows.",
                    )
parser.add_argument("-de", "--default",
                    action="store_true",
                    help="Apply default operators.",
                    )
parser.add_argument("-mu", "--multislice",
                    type=str,
                    help="Apply only slices.",
                    )
parser.add_argument("-or", "--orbit",
                    type=str,
                    help="Gather orbital view (vertical/horizontal/both).",
                    )
parser.add_argument("-se", "--sessionreplacesingle",
                    type=str,
                    help="Replace loaded data from a session file.",
                    )
parser.add_argument("-sm", "--sessionreplacemultiple",
                    type=str,
                    help="Replace loaded data from multiple session files.",
                    )
parser.add_argument("-gi", "--grabimagesfromsessions",
                    action="store_true",
                    help="Load sessions and grab window images.",
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

if args.dataconvertstl:
    BashCommand = args.dataconvertstl
    FileBash = BashOptions(BashCommand)
    FileBash.DataConvert()

if args.dataconvertvtk:
    BashCommand = args.dataconvertvtk
    FileBash = BashOptions(BashCommand)
    FileBash.DataConvert()

if args.graveremove:
    BashCommand = args.graveremove
    FileBash = BashOptions(BashCommand)
    FileBash.GraveRemove()

if args.surfaces:
    BashCommand = args.surfaces
    FileBash = BashOptions(BashCommand)
    FileBash.Surfaces()

if args.curves:
    BashCommand = args.curves
    FileBash = BashOptions(BashCommand)
    FileBash.Curves()

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
print "Elapsed time was "+str(ElapsedTime)+" seconds."
