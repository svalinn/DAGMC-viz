from visit import *


def OperatorSlice(
                  File,
                  OperSet,
                  OperOptions,
                  Centroids,
                  PlottingSpatialExtents,
                  SinglePlane=1
                  ):
    """
    with no args - default direction and location
    [(<x,y,z>,val),(<x,y,z>,val),....]
    produces one image for each tuple with slice at plane <x,y,z>=val
    A warning is raised for exceeding pseudocolor plot bounds.
    """

    ResetView()
    AddOperator(OperSet.title(), 1)
    SetActivePlots((tuple(range(0, len(File)))))

    try:

        xmin = PlottingSpatialExtents["Pseudocolor"][0]
        xmax = PlottingSpatialExtents["Pseudocolor"][1]
        ymin = PlottingSpatialExtents["Pseudocolor"][2]
        ymax = PlottingSpatialExtents["Pseudocolor"][3]
        zmin = PlottingSpatialExtents["Pseudocolor"][4]
        zmax = PlottingSpatialExtents["Pseudocolor"][5]

    except Exception:
        pass

    if OperOptions is not None:
        OperOptions = list(OperOptions)

        Attribute = SliceAttributes()

        Attribute.project2d = SinglePlane

        try:
            if OperOptions[1]:

                Attribute.originType = Attribute.Point

                if OperOptions[0].lower() == "x":
                    try:
                        if OperOptions[1] < xmin:
                            print "Slice chosen below minimum x value."
                        elif OperOptions[1] > xmax:
                            print "Slice chosen above maximum x value."
                    except Exception:
                        pass

                    Attribute.originPoint = (OperOptions[1], 0, 0)

                if OperOptions[0].lower() == "y":
                    try:
                        if OperOptions[1] < ymin:
                            print "Slice chosen below minimum y value."
                        elif OperOptions[1] > ymax:
                            print "Slice chosen above maximum y value."
                    except Exception:
                        pass

                    Attribute.originPoint = (0, OperOptions[1], 0)

                if OperOptions[0].lower() == "z":
                    try:
                        if OperOptions[1] < zmin:
                            print "Slice chosen below minimum z value."
                        elif OperOptions[1] > zmax:
                            print "Slice chosen above maximum z value."
                    except Exception:
                        pass

                    Attribute.originPoint = (0, 0, OperOptions[1])

        except Exception:
                Attribute.originType = Attribute.Point

                if OperOptions[0].lower() == "x":
                    Attribute.originPoint = (Centroids["Pseudocolor"][0], 0, 0)

                if OperOptions[0].lower() == "y":
                    Attribute.originPoint = (0, Centroids["Pseudocolor"][1], 0)

                if OperOptions[0].lower() == "z":
                    Attribute.originPoint = (0, 0, Centroids["Pseudocolor"][2])

        Attribute.axisType = eval(
                                  "Attribute." +
                                  str(OperOptions[0]).upper() +
                                  "Axis"
                                  )

        SetOperatorOptions(Attribute)


def OperatorClip(File, OperSet, OperOptions, Centroids):
    """
    With no args - default octant, rotation and midpoint
    [{loc:(x,y,z),oct:(+/-1,+/-1,+/-1),rot:(xdeg,ydeg,zdeg)},...]
    produces one image for each dictionary.

    Clip must be applied last for the view effect to work.
    """

    ResetView()
    AddOperator(OperSet.title(), 1)
    SetActivePlots((tuple(range(0, len(File)))))

    if OperOptions is not None:
        OperOptions = dict(OperOptions)

        Attribute = ClipAttributes()

        Attribute.quality = Attribute.Accurate

        Attribute.plane1Status = 1  # yz-plane
        Attribute.plane2Status = 1  # xz-plane
        Attribute.plane3Status = 1  # xy-plane

        if "loc" in OperOptions:
            xpos = OperOptions["loc"][0]
            ypos = OperOptions["loc"][1]
            zpos = OperOptions["loc"][2]

            Attribute.plane1Origin = (xpos, 0, 0)
            Attribute.plane2Origin = (0, ypos, 0)
            Attribute.plane3Origin = (0, 0, zpos)

        else:
            Centroids = dict(Centroids)

            Attribute.plane1Origin = (Centroids["Pseudocolor"][0], 0, 0)
            Attribute.plane2Origin = (0, Centroids["Pseudocolor"][1], 0)
            Attribute.plane3Origin = (0, 0, Centroids["Pseudocolor"][2])

        Attribute.plane1Normal = (OperOptions["oct"][0], 0, 0)
        Attribute.plane2Normal = (0, OperOptions["oct"][1], 0)
        Attribute.plane3Normal = (0, 0, OperOptions["oct"][2])

        if "rot" in OperOptions:
            xdeg = OperOptions["rot"][0]
            ydeg = OperOptions["rot"][1]
            zdeg = OperOptions["rot"][2]

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
                            OperOptions["oct"][0],
                            OperOptions["oct"][1],
                            OperOptions["oct"][2],
                            )

            SetView3D(v)

        SetOperatorOptions(Attribute)


def OperatorThreshold(OperSet, OperOptions, tags):
    """
    expr = plottype > val | plottype < val | plottype = (min,max)
    """

    ResetView()
    SetActivePlots(tags[OperOptions[0].title()])
    AddOperator(OperSet.title(), 0)

    if OperOptions is not None:
        OperOptions = list(OperOptions)
        Bounds = eval(OperOptions[2])

        Attribute = ThresholdAttributes()

        if OperOptions[1] == "=":
            Attribute.lowerBounds = Bounds[0]
            Attribute.upperBounds = Bounds[1]

        if OperOptions[1] == ">":
            Attribute.lowerBounds = Bounds

        if OperOptions[1] == "<":
            Attribute.upperBounds = Bounds

        SetOperatorOptions(Attribute)
