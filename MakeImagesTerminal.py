import argparse
import timeit

import Iterator as It

tic = timeit.default_timer()

parser = argparse.ArgumentParser(description="Terminal execution of tool.",
                                 usage="Create plots to save.",
                                 )

parser.add_argument("-i", "--iterations",
                    nargs="?",
                    default=1,
                    type=int,
                    help="add plots of data",
                    )
parser.add_argument("-o", "--operator",
                    nargs="?",
                    default="None",
                    type=str,
                    help="settings for plots and operators",
                    )
parser.add_argument("-v", "--view",
                    nargs="+",
                    type=float,
                    help="change view (x,y,z) in degrees",
                    )

args = parser.parse_args()

if args.iterations:
    Number=args.iterations

if args.operator:
    OperatorSet=args.operator

if args.view:
    Coordinates = tuple(args.view)
    Coordinates=Coordinates
else:
    Coordinates = tuple((0.0, 0.0, 0.0))

It.Iterator(Number, OperatorSet, Coordinates)

toc = timeit.default_timer()
ElapsedTime = toc - tic
print("Elapsed time was "+str(ElapsedTime)+" seconds.")
