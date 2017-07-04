import argparse
import timeit

import MultipleWindows as Mu

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

args = parser.parse_args()

if args.plot:
    FilePlots = input("Insert list of plot lists: ")

if args.operator:
    OperatorSet = input("Insert list of operator lists: ")

tic = timeit.default_timer()  # Start timer.


if args.windows:
    try:
        Mu.MultipleWindows(FilePlots, OperatorSet, Windows=True)
    except Exception:
        Mu.MultipleWindows(FilePlots, Windows=True)

else:
    try:
        Mu.MultipleWindows(FilePlots, OperatorSet)
    except Exception:
        Mu.MultipleWindows(FilePlots)


toc = timeit.default_timer()  # End timer.
ElapsedTime = toc - tic
print("Elapsed time was "+str(ElapsedTime)+" seconds.")
