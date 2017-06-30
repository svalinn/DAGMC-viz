import argparse
import timeit

import Iterator as It

from Inputs import *

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

args = parser.parse_args()

if args.plot:
    FilePlots = input("Insert list of plot lists: ")

if args.operator:
    OperatorSet = input("Insert list of operator lists: ")

tic = timeit.default_timer()  # Start timer.

try:
    It.Iterator(Files, Operators)
except Exception:
    pass

try:
    It.Iterator(Files)
except Exception:
    pass

toc = timeit.default_timer()  # End timer.
ElapsedTime = toc - tic
print("Elapsed time was "+str(ElapsedTime)+" seconds.")
