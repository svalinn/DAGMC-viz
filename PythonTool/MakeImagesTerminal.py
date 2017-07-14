import argparse
import timeit
import ast

import MultipleWindows as Mw
import MultiSlice as Ms
import Orbit as Or

parser = argparse.ArgumentParser(description="Terminal execution of tool.",
                                 usage="Create plots to save.",
                                 )

parser.add_argument("-p", "--plots",
                    type=str,
                    help="List of plots.",
                    )
parser.add_argument("-o", "--operators",
                    type=str,
                    help="List of operators.",
                    )
parser.add_argument("-i", "--images",
                    action="store_true",
                    help="Make images of plots and operators.",
                    )
parser.add_argument("-w", "--windows",
                    action="store_true",
                    help="Open multiple windows.",
                    )
parser.add_argument("-d", "--default",
                    action="store_true",
                    help="Apply default operators.",
                    )
parser.add_argument("-m", "--multislice",
                    type=str,
                    help="Apply only slices.",
                    )
parser.add_argument("-O", "--orbit",
                    type=str,
                    help="Gather orbital view (vertical/horizontal/both).",
                    )

args = parser.parse_args()

# Gather plot and operator inputs.
FilePlots = ast.literal_eval(args.plots)

if args.operators:
    OperatorSet = ast.literal_eval(args.operators)

if args.images:

    tic = timeit.default_timer()  # Start timer.

    try:
        Mw.MultipleWindows(FilePlots, OperatorSet, Windows=False)
    except Exception:
        Mw.MultipleWindows(FilePlots, Windows=False)


if args.windows:
   
    tic = timeit.default_timer()  # Start timer.

    try:
        Mw.MultipleWindows(FilePlots, OperatorSet, Windows=True)
    except Exception:
        Mw.MultipleWindows(FilePlots, Windows=True)

if args.default:

    OperatorSet = [
                  ["Slice", ("x")],
                  ["Slice", ("y")],
                  ["Slice", ("z")],
                  [{"Clip": {"oct": (1, 1, 1)}}],
                  ]

    tic = timeit.default_timer()  # Start timer.
    Mw.MultipleWindows(FilePlots, OperatorSet, Windows=True)

if args.multislice:
    Axis = ast.literal_eval(args.multislice)[0]
    Number = ast.literal_eval(args.multislice)[1]
    myList = (str(Axis), int(Number))

    tic = timeit.default_timer()  # Start timer.
    Ms.MultiSlice(FilePlots, myList)

if args.orbit:
    print ast.literal_eval(args.orbit)[0]
    Statement = ast.literal_eval(args.orbit)[0]

    try:
        if OperatorSet is None:
            OperatorSet = False
    except Exception:
        pass

    Direction = ast.literal_eval(args.orbit)[1]
    Iteration = ast.literal_eval(args.orbit)[2]

    tic = timeit.default_timer()  # Start timer.
    Or.Orbit(FilePlots, (Direction, Iteration), OperatorSet)

toc = timeit.default_timer()  # End timer.
ElapsedTime = toc - tic
print("Elapsed time was "+str(ElapsedTime)+" seconds.")
