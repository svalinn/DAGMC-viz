import visit as Vi

Vi.Launch()  # Here to allow import of other modules.

import PathCreator as Pa
import MakeImagesPython as Mk


def Orbit(Files, myList):
    """
    Take multiple views around Vertically or Horizontally.
    Views are evenly spaced.
    myList = (<axis>, <number of views>).

    The higher the number of views the smoother the rotation.

    This assumes the following positive axis orientation:
    y - Up
    x - Right
    z - Out from screen
    """

    Pa.PathCreator()  # Creates necessary folders.

    myList = tuple(myList)

    Line = str(myList[0])
    Number = int(myList[1])

    if myList[0].lower() == "vertical":
        Line = 0
        ViewN = (0, 0, 1)
        ViewU = (0, 1, 0)

    if myList[0].lower() == "horizontal":
        Line = 1
        ViewN = (0, 0, 1)
        ViewU = (0, 1, 0)

    Increment = 360.0/float(Number)  # Degrees

    Image = Mk.MakeImages(Files)
    Image.Plot()

    v = Vi.GetView3D()
    v.viewNormal = ViewN
    v.viewUp = ViewU

    Degrees = 0
    while 360.0 > Degrees:
        # Turning shading False yields black images.
        Image.Save(Shading=True)
        v.RotateAxis(Line, Increment)
        Vi.SetView3D(v)
        Degrees += Increment
