from visit import *
import MakeImagesPython as Mk
import PathCreator as Pa
import Inputs

Image = Mk.MakeImages(Inputs.Files)

Image.Plot()


def Iterator(Number=1, OperatorSet=None, Coordinates=None):
    """Iterate through several operator options."""

    Pa.PathCreator()  # Creates necessary folders.

    for item in range(0, Number):

        if not OperatorSet == None:
            Image.Operator(OperatorSet)
            Image.Settings(OperatorSet+str(item))

        Image.Save(Coordinates)
