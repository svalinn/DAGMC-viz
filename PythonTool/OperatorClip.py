from visit import *


def OperatorClip(File, OperSet, myList, Centroids):
    """
    With no args - default octant, rotation and midpoint
    [{loc:(x,y,z),oct:(+/-1,+/-1,+/-1),rot:(xdeg,ydeg,zdeg)},...]
    produces one image for each dictionary.

    If multiple clips are used, define the rotation key.
    """

    ResetView()
    AddOperator(OperSet.title(), 1)
    SetActivePlots((tuple(range(0, len(File)))))

    if myList is not None:
        myList = dict(myList)

        Attribute = ClipAttributes()

        Attribute.quality = Attribute.Accurate

        Attribute.plane1Status = 1  # yz-plane
        Attribute.plane2Status = 1  # xz-plane
        Attribute.plane3Status = 1  # xy-plane

        if "loc" in myList:
            xpos = myList["loc"][0]
            ypos = myList["loc"][1]
            zpos = myList["loc"][2]

            Attribute.plane1Origin = (xpos, 0, 0)
            Attribute.plane2Origin = (0, ypos, 0)
            Attribute.plane3Origin = (0, 0, zpos)

        else:
            Centroids = dict(Centroids)

            Attribute.plane1Origin = (Centroids["Pseudocolor"][0], 0, 0)
            Attribute.plane2Origin = (0, Centroids["Pseudocolor"][1], 0)
            Attribute.plane3Origin = (0, 0, Centroids["Pseudocolor"][2])

        Attribute.plane1Normal = (myList["oct"][0], 0, 0)
        Attribute.plane2Normal = (0, myList["oct"][1], 0)
        Attribute.plane3Normal = (0, 0, myList["oct"][2])

        if "rot" in myList:
            xdeg = myList["rot"][0]
            ydeg = myList["rot"][1]
            zdeg = myList["rot"][2]

            ResetView()

            # Set view
            v = GetView3D()

            v.RotateAxis(0, float(xdeg))  # rotate around x-axis
            v.RotateAxis(1, float(ydeg))  # rotate around y-axis
            v.RotateAxis(2, float(zdeg))  # rotate around z-axis

            SetView3D(v)

        else:
            ResetView()

            # Set view
            v = GetView3D()

            v.viewNormal = (
                            myList["oct"][0],
                            myList["oct"][1],
                            myList["oct"][2],
                            )

            SetView3D(v)

        SetOperatorOptions(Attribute)
