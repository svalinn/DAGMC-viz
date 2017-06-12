import argparse

import MakeImagesPython
import Inputs


parser = argparse.ArgumentParser(
    description='Terminal execution of tool.',
    usage='Remains to be seen.',
    )

parser.add_argument("--Plot",
                    help="add plots of data")
parser.add_argument("--Operator",
                    help="add operators")
parser.add_argument("--Settings",
                    help="settings for plots and operators")
parser.add_argument("--Save",
                    help="save display")

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
