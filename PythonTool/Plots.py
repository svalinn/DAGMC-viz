from visit import *


def PlotMesh(File, ObjectSequence):
    # Mesh plot attributes.

    Attribute = MeshAttributes()  # Enables changing plot attributes.

    if File is not None:
        File = list(File)

        Attribute.showInternal = 1  # Show internal geometry of a mesh.

        for item in File:
            if item[1].title() == "Mesh":
                # Check for optional inputs in Dictionary input.
                try:
                    # Change the options for line style.
                    Attribute.lineStyle = eval(
                                               "Attribute." +
                                               str(item[3]).upper()
                                               )
                except Exception:
                    pass

    SetPlotOptions(Attribute)  # Apply changed attributes.


def PlotPseudocolor(File, ObjectSequence):
    # Pseudocolor plot attributes.

    # Change orientation of legend and font.
    LegendAttributes = GetAnnotationObject(ObjectSequence["Pseudocolor"])
    LegendAttributes.orientation = "VerticalLeft"
    LegendAttributes.fontHeight = 0.03

    Attribute = PseudocolorAttributes()  # Enables changing plot attributes.

    if File is not None:
        File = list(File)

        for item in File:
            if item[1].title() == "Pseudocolor":

                # Check for optional inputs.
                try:
                    # Can choose linear or logarithmic scaling for the plot.
                    Attribute.scaling = eval(
                                             "Attribute." +
                                             str(item[3]).title()
                                             )
                except Exception:
                    pass

                # Change how colors scale based on defined data values.
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

    SetPlotOptions(Attribute)  # Apply changed attributes.


def PlotContour(File, ObjectSequence):
    # Contour plot attributes.

    # Change orientation of legend and font.
    LegendAttributes = GetAnnotationObject(ObjectSequence["Contour"])
    LegendAttributes.orientation = "VerticalLeft"
    LegendAttributes.fontHeight = 0.03

    Attribute = ContourAttributes()  # Enables changing plot attributes.

    if File is not None:
        File = list(File)

        for item in File:
            if item[1].title() == "Contour":

                # Check for optional inputs.
                try:
                    # Change the options for line style.
                    Attribute.lineStyle = eval(
                                               "Attribute." +
                                               str(item[3]).upper()
                                               )
                except Exception:
                    pass

    SetPlotOptions(Attribute)  # Apply changed attributes.
