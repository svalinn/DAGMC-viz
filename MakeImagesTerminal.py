import argparse
import timeit

import MakeImagesPython
import Inputs

tic = timeit.default_timer()

parser = argparse.ArgumentParser(description="Terminal execution of tool.",
                                 usage="Create plots to save.",
                                 )

parser.add_argument("-pl", "--Plot",
                    help="add plots of data",
                    action="store_true",
                    )

parser.add_argument("-op", "--Operator",
                    nargs="?",
                    const="NoOperator",
                    type=str,
                    help="settings for plots and operators",
                    )
parser.add_argument("-se", "--Settings",
                    help="add operators",
                    action="store_true",
                    )
parser.add_argument("-vi", "--View",
                    nargs="+",
                    type=float,
                    help="change view (x,y,z) in degrees",
                    )
parser.add_argument("-sa", "--Save",
                    help="save display",
                    action="store_true",
                    )

args = parser.parse_args()

Image = MakeImagesPython.MakeImages(Inputs.Files)

OperatorSet = args.Operator

if args.Plot:
    Image.Plot()

    if args.Operator:
        Image.Operator(OperatorSet)

    if args.Settings:
        Image.Settings(OperatorSet)

    if args.View:
        Coordinates = tuple(args.View)
    else:
        Coordinates = (0.0, 0.0, 0.0)

    if args.Save:
        Image.Save(Coordinates)

toc = timeit.default_timer()
ElapsedTime = toc - tic

print("Elapsed time was "+str(ElapsedTime)+" Seconds")
