import argparse

import MakeImagesPython
import Inputs


parser = argparse.ArgumentParser(
    description='Terminal execution of tool.',
    usage='Create plots to save with or without operators and settings.',
    )

parser.add_argument("--Plot",
                    help="add plots of data",
                    action="store_true",
                    )
parser.add_argument("--Operator",
                    help="add operators",
                    action="store_true",
                    )
parser.add_argument("--Settings",
                    help="settings for plots and operators",
                    action="store_true",
                    )
parser.add_argument("--Save",
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
