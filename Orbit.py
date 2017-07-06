import visit as Vi

import Iterator as It
import PathCreator as Pa


def Orbit(Files, myList):
    """
    Take multiple views around an axis.
    Views are evenly spaced.
    myList = (<axis>, <number of views>).
    """

    Pa.PathCreator()  # Creates necessary folders.

    myList = tuple(myList)

    Axis = str(myList[0])
    Number = int(myList[1])

    Increment = 360.0/float(Number)  # Degrees

    Distance = 0
    OperatorSet = []
    while 360.0 > Distance:

        OperatorSet.append(["Transform", (Axis, Distance)])

        Distance += Increment

    It.Iterator(Files, OperatorSet)
    print OperatorSet
