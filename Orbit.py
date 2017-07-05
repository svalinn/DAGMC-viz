import math as Ma
import scipy as Sc
import visit as Vi

Vi.Launch()

import PathCreator as Pa
import MakeImagesPython as Mk


def Orbit(File, myList):
    """
    Take multiple views around an axis.
    Views are evenly spaced.
    myList = (<axis>, <number of views>).
    """

    Pa.PathCreator()  # Creates necessary folders.

    myList = tuple(myList)

    Axis = str(myList[0])
    Number = int(myList[1])

    Image = Mk.MakeImages(File)
    Image.Plot()
    Image.Operator("Clip")

    Increment = (2*Sc.pi)/float(Number)

    Vi.ResetView()

    # Set view
    v = Vi.GetView3D()

    Count = 0
    Distance = 0
    RotList = []
    while 2*Sc.pi > Distance:  # Problem with accuracy
        v1 = Ma.cos(Distance)
        v2 = Ma.sin(Distance)
        Position = (v1, v2)
        RotList.append(Position)

        Count += 1
        if Count == 0:
            Distance = 0
        else:
            Distance += Increment

    for item in RotList:
        if Axis.lower() == "x":
            v.viewNormal = (0, item[0], item[1])
            print item
            Vi.SetView3D(v)

        if Axis.lower() == "y":
            v.viewNormal = (item[0], 0, item[1])
            Vi.SetView3D(v)

        if Axis.lower() == "z":
            v.viewNormal = (item[0], item[1], 0)
            Vi.SetView3D(v)

        Image.Save()

    Vi.SetView3D(v)
