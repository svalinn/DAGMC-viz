import visit as Vi

Vi.Launch()

import PathCreator as Pa
import MakeImagesPython as Mk


def Orbit(Files, myList):
    """
    Take multiple views around an axis.
    Views are evenly spaced.
    myList = (<axis>, <number of views>).
    """

    Pa.PathCreator()  # Creates necessary folders.

    myList = tuple(myList)

    Line = str(myList[0])
    Number = int(myList[1])

    if myList[0].lower() == "x":
        Line = 0
        ViewN = (0, 0, 1)
        ViewU = (0, 1, 0)

    if myList[0].lower() == "y":
        Line = 1
        ViewN = (0, 0, 1)
        ViewU = (0, 1, 0)

    if myList[0].lower() == "z":
        Line = 1
        ViewN = (1, 0, 0)
        ViewU = (0, 0, 1)

    Increment = 360.0/float(Number)  # Degrees

    Image = Mk.MakeImages(Files)
    Image.Plot()

    v = Vi.GetView3D()
    v.viewNormal = ViewN
    v.viewUp = ViewU

    for item in range(Number):
        v.RotateAxis(Line, Increment)
        Vi.SetView3D(v)
        Image.Save(Shading=True)
