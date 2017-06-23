from visit import *


def OperatorSettings(OperatorSet, myList):
    """Add operator and its settings."""

    myList = list(myList)

    if OperatorSet == "Clip":
        """
        with no args - default octant, rotation and midpoint
        [{loc:(x,y,z),octant:(+/-1,+/-1,+/-1),rot:(alpha,beta,gamma)},...]
        produces one image for each dictionary
        """

        Attribute = ClipAttributes()

        x = myList[loc][0]
        y = myList[loc][1]
        z = myList[loc][2]

        Attribute.quality = Attribute.Accurate

        Attribute.plane1Status = 1  # yz-plane
        Attribute.plane2Status = 1  # xz-plane
        Attribute.plane3Status = 1  # xy-plane

        Attribute.plane1Normal = (myList[octant][0], 0, 0)
        Attribute.plane2Normal = (0, myList[octant][1], 0)
        Attribute.plane3Normal = (0, 0, myList[octant][2])

        alpha = myList[rot][0]
        beta = myList[rot][1]
        gamma = myList[rot][2]

        # Convert the cartesian coordinates to polar coordinates

        ResetView()

        # Set view
        v = GetView3D()

        v.RotateAxis(0, xdeg)  # x-axis
        v.RotateAxis(1, ydeg)  # y-axis
        v.RotateAxis(2, zdeg)  # z-axis

        SetView3D(v)

        SetOperatorOptions(Attribute)

    if OperatorSet == "Slice":
        """
        with no args - default direction and location
        [(<x,y,z>,val),(<x,y,z>,val),....]
        produces one image for each tuple with slice at plane <x,y,z>=val
        """

        Attribute = SliceAttributes()

        x = myList[0][0]
        y = myList[0][1]
        z = myList[0][2]

        Attribute.originType = Attribute.Point
        Attribute.originPoint = (x, y, z)

        Attribute.axisType = eval("Attribute."+str(myList[1]).upper()+"Axis")

        SetOperatorOptions(Attribute)
