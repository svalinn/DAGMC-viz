import argparse
import timeit

import MultipleWindows as Mw
import MultiSlice as Ms

parser = argparse.ArgumentParser(description="Terminal execution of tool.",
                                 usage="Create plots to save.",
                                 )

parser.add_argument("-p", "--plot",
                    action="store_true",
                    help="Add plots with settings.",
                    )
parser.add_argument("-o", "--operator",
                    action="store_true",
                    help="Add operators with settings.",
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

args = parser.parse_args()

if args.plot:
    FilePlots = input("Insert list of plot lists: ")

if args.operator:
    OperatorSet = input("Insert list of operator lists: ")

tic = timeit.default_timer()  # Start timer.


if args.windows:
    try:
        Mw.MultipleWindows(FilePlots, OperatorSet, Windows=True)
    except Exception:
        w.MultipleWindows(FilePlots, Windows=True)

if args.default:
    OperatorSet = [
                  ["Slice", ("x")],
                  ["Slice", ("y")],
                  ["Slice", ("z")],
                  [{"Clip": {"oct": (1, 1, 1)}}],
                  ]

    Mw.MultipleWindows(FilePlots, OperatorSet, Windows=True)

if args.multislice:
    FilePlots = input("Insert list of plot lists: ")
    Axis = raw_input("Insert axis for slicing: ")
    Number = raw_input("Insert number of slices: ")
    myList = (str(Axis), int(Number))
    Ms.MultiSlice(FilePlots, myList)

toc = timeit.default_timer()  # End timer.
ElapsedTime = toc - tic
print("Elapsed time was "+str(ElapsedTime)+" seconds.")
