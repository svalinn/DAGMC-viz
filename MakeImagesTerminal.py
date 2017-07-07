import argparse
import timeit

import MultipleWindows as Mw
import MultiSlice as Ms
import Orbit as Or

parser = argparse.ArgumentParser(description="Terminal execution of tool.",
                                 usage="Create plots to save.",
                                 )

parser.add_argument("-i", "--images",
                    action="store_true",
                    help="Make Images of plots and operators.",
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
                    action="store_true",
                    help="Apply only slices.",
                    )
parser.add_argument("-o", "--orbit",
                    action="store_true",
                    help="Gather orbital view.",
                    )

args = parser.parse_args()

if args.images:
    FilePlots = input("Insert list of plot lists: ")
    Statement = raw_input("Add operators? (yes/no): ")

    if Statement.lower() == "yes":
        OperatorSet = input("Insert list of operator lists: ")
    else:
        pass

    tic = timeit.default_timer()  # Start timer.

    try:
        Mw.MultipleWindows(FilePlots, OperatorSet, Windows=False)
    except Exception:
        Mw.MultipleWindows(FilePlots, Windows=False)


if args.windows:
    FilePlots = input("Insert list of plot lists: ")
    Statement = raw_input("Add operators? (yes/no): ")

    if Statement.lower() == "yes":
        OperatorSet = input("Insert list of operator lists: ")
    else:
        pass

    tic = timeit.default_timer()  # Start timer.

    try:
        Mw.MultipleWindows(FilePlots, OperatorSet, Windows=True)
    except Exception:
        Mw.MultipleWindows(FilePlots, Windows=True)

if args.default:
    FilePlots = input("Insert list of plot lists: ")

    OperatorSet = [
                  ["Slice", ("x")],
                  ["Slice", ("y")],
                  ["Slice", ("z")],
                  [{"Clip": {"oct": (1, 1, 1)}}],
                  ]

    tic = timeit.default_timer()  # Start timer.
    Mw.MultipleWindows(FilePlots, OperatorSet, Windows=True)

if args.multislice:
    FilePlots = input("Insert list of plot lists: ")
    Axis = raw_input("Insert axis for slicing (x/y/z): ")
    Number = raw_input("Insert number of slices: ")
    myList = (str(Axis), int(Number))

    tic = timeit.default_timer()  # Start timer.
    Ms.MultiSlice(FilePlots, myList)

if args.orbit:
    FilePlots = input("Insert list of plot lists: ")
    Direction = raw_input("Orbit? (vertical/horizontal/both): ")
    Iteration = raw_input("Number of views in orbit?: ")

    tic = timeit.default_timer()  # Start timer.
    Or.Orbit(FilePlots, (Direction, Iteration))

toc = timeit.default_timer()  # End timer.
ElapsedTime = toc - tic
print("Elapsed time was "+str(ElapsedTime)+" seconds.")
