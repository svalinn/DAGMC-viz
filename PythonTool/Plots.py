from visit import *

from GeneratePlotAttributes import *


def PlotMesh(File):
    # Mesh plot attributes.

    Attribute = MeshAttributes()  # Enables changing plot attributes.

    Attribute.showInternal = 1  # Show internal geometry of a mesh.

    # Check for optional inputs in Dictionary input.
    try:
        # Change the options for line style.
        exec(GeneratePlotAttributes(File)["Mesh"])

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
                # The item[4] in the following indicate whether
                # an option at the end of an inserted pseudocolor plot
                # will take effect.
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

    # Check for optional inputs in Dictionary input.
    try:
        # Change the options for line style.
        exec(GeneratePlotAttributes(File)["Contour"])

    except Exception:
        pass

    SetPlotOptions(Attribute)  # Apply changed attributes.
