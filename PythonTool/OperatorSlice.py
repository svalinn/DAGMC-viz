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
