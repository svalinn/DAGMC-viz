import visit as Vi

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

    Increment = 360.0/float(Number)  # Degrees

    Image = Mk.MakeImages(Files)
    Image.Plot()

    # Choose which orbits to do.
    if myList[0].lower() == "both":
        newList = ["vertical", "horizontal"]
    elif myList[0].lower() == "vertical":
        newList = ["vertical", "NaN"]
    elif myList[0].lower() == "horizontal":
        newList = ["NaN", "horizontal"]

    # Vertical orbit.
    Vi.ResetView()
    try:
        if newList[0].lower() == "vertical":
            LineV = 0
            ViewNV = (0, 0, 1)
            ViewUV = (0, 1, 0)

            v = Vi.GetView3D()
            v.viewNormal = ViewNV
            v.viewUp = ViewUV

            Degrees = 0
            while 360.0 > Degrees:
                # Turning shading False yields black images.
                Image.Save(Shading=True)
                v.RotateAxis(LineV, Increment)
                Vi.SetView3D(v)
                Degrees += Increment
    except Exception:
        pass

    # Horizontal orbit.
    Vi.ResetView()
    try:
        if newList[1].lower() == "horizontal":
            LineH = 1
            ViewNH = (0, 0, 1)
            ViewUH = (0, 1, 0)

            v = Vi.GetView3D()
            v.viewNormal = ViewNH
            v.viewUp = ViewUH

            Degrees = 0
            while 360.0 > Degrees:
                # Turning shading False yields black images.
                Image.Save(Shading=True)
                v.RotateAxis(LineH, Increment)
                Vi.SetView3D(v)
                Degrees += Increment
    except Exception:
        pass
