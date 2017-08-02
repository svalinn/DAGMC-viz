from visit import *


def PlotMesh(File, ObjectSequence):
    # Mesh plot attributes.

    Attribute = MeshAttributes()

    if File is not None:
        File = list(File)

        Attribute.showInternal = 1

        for item in File:
            if item[1].title() == "Mesh":
                # Check for optional inputs in Dictionary input.
                try:
                    Attribute.lineStyle = eval(
                                               "Attribute." +
                                               str(item[3]).upper()
                                               )
                except Exception:
                    pass

    SetPlotOptions(Attribute)


def PlotPseudocolor(File, ObjectSequence):
    # Pseudocolor plot attributes.

    # Change orientation of legend
    LegendAttributes = GetAnnotationObject(ObjectSequence["Pseudocolor"])
    LegendAttributes.orientation = "VerticalLeft"
    LegendAttributes.fontHeight = 0.03

    Attribute = PseudocolorAttributes()

    if File is not None:
        File = list(File)

        for item in File:
            if item[1].title() == "Pseudocolor":

                # Check for optional inputs in Dictionary input.
                try:
                    Attribute.scaling = eval(
                                             "Attribute." +
                                             str(item[3]).title()
                                             )
                except Exception:
                    pass

                try:

                    if (item[4])[0].title() == "Min":
                        Attribute.min = item[4][1]
                        Attribute.minFlag = 1
                except Exception:
                    pass

                try:
                    if (item[4])[0].title() == "Min":
                        Attribute.max = item[5][1]
                        Attribute.maxFlag = 1
                except Exception:
                    pass

                try:
                    if (item[4])[0].title() == "Max":
                        Attribute.max = item[4][1]
                        Attribute.maxFlag = 1
                except Exception:
                    pass

    SetPlotOptions(Attribute)


def PlotContour(File, ObjectSequence):
    # Contour plot attributes.

    # Change orientation of legend
    LegendAttributes = GetAnnotationObject(ObjectSequence["Contour"])
    LegendAttributes.orientation = "VerticalLeft"
    LegendAttributes.fontHeight = 0.03

    Attribute = ContourAttributes()

    Attribute.legendFlag = 1

    if File is not None:
        File = list(File)

        for item in File:
            if item[1].title() == "Contour":

                # Check for optional inputs in Dictionary input.
                try:
                    Attribute.lineStyle = eval(
                                               "Attribute." +
                                               str(item[3]).upper()
                                               )
                except Exception:
                    pass

    SetPlotOptions(Attribute)
