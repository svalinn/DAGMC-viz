import visit as Vi

import Iterator as It
import PathCreator as Pa
import MakeImagesPython as Mk


def Orbit(Files, myList, OperatorSet=False):
    """
    Take multiple views around vertically, horizontally, or both.
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

    # Multiple Operators.
    try:
        for multiitem in OperatorSet:

            # Apply dictionary operator.
            try:
                Operator = (multiitem.keys())[0]
                List = (multiitem.values())[0]
                Image.Operator(Operator, List, SliceProject=0)
            except Exception:
                pass

            # Apply list operator.
            try:
                Operator = multiitem[0]
                List = multiitem[1]
                Image.Operator(Operator, List, SliceProject=0)
            except Exception:
                pass

    except Exception:
        pass

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
