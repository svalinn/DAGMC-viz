from visit import *


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
