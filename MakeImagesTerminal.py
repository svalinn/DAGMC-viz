import argparse
import timeit

import MakeImagesPython
import Inputs

tic = timeit.default_timer()

parser = argparse.ArgumentParser(
                                description='Terminal execution of tool.',
                                usage='Create plots to save with or without operators and settings.',
                                )

parser.add_argument("-pl", "--Plot",
                    help="add plots of data",
                    action="store_true",
                    )
parser.add_argument("-op", "--Operator",
                    help="add operators",
                    action="store_true",
                    )
parser.add_argument("-se", "--Settings",
                    help="settings for plots and operators",
                    action="store_true",
                    )
parser.add_argument("-sa", "--Save",
                    help="save display",
                    action="store_true",
                    )

args = parser.parse_args()

Image = MakeImagesPython.MakeImages(Inputs.Files, Inputs.Operators)


if args.Plot:
    Image.Plot()

    if args.Operator:
        Image.Operator()

    if args.Settings:
        Image.Settings()

    if args.Save:
        Image.Save()

toc = timeit.default_timer()
ElapsedTime = toc - tic

print("Elapsed time was "+str(ElapsedTime)+" Seconds")
