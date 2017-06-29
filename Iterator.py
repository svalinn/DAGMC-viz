from visit import *
import MakeImagesPython as Mk
import PathCreator as Pa
import Inputs as In

Image = Mk.MakeImages(In.Files)
Operators = In.Operators

Image.Plot()


def Iterator(OperatorSet=None, myList=None):
    """Iterate through several operator options."""

    Pa.PathCreator()  # Creates necessary folders.

    for item in Operators:
        if OperatorSet is not None:
            Operator = (item.keys())[0]
            myList = (item.values())[0]
            Image.Operator(Operator, myList)
            Image.Save()
