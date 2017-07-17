import argparse
import timeit
import ast

from TerminalOptions import TerminalOptions

tic = timeit.default_timer()  # Start timer.

parser = argparse.ArgumentParser(description="Terminal execution of tool.",
                                 usage="Create plots to save.",
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
parser.add_argument("-da", "--dataconvert",
                    type=str,
                    help="Convert file formats using mbconvert.",
                    )
parser.add_argument("-gr", "--graveremove",
                    action="store_true",
                    help="Remove grave yard from mesh.",
                    )
parser.add_argument("-su", "--surfaces",
                    action="store_true",
                    help="Create curve file from h5m file.",
                    )
parser.add_argument("-cu", "--curves",
                    action="store_true",
                    help="Create curve file from h5m file.",
                    )
parser.add_argument("-se", "--sessionreplace",
                    action="store_true",
                    help="Replace loaded data from sessions.",
                    )

args = parser.parse_args()

# Gather plot and operator inputs.
FilePlots = ast.literal_eval(args.plots)

if args.operators:
    OperatorSet = ast.literal_eval(args.operators)
    Options = TerminalOptions(args, FilePlots, OperatorSet)

else:
    Options = TerminalOptions(args, FilePlots)

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

if args.dataconvert:
    Options.DataConvert()

if args.graveremove:
    Options.GraveRemove()

if args.surfaces:
    Options.Surfaces()

if args.orbit:
    Options.curves()

if args.sessionreplace:
    Options.SessionReplace()

toc = timeit.default_timer()  # End timer.
ElapsedTime = toc - tic
print("Elapsed time was "+str(ElapsedTime)+" seconds.")
