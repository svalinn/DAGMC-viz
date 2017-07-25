from visit import *


def PlotContour(File):
    # Contour plot attributes.

    Attribute = ContourAttributes()

    Attribute.legendFlag = 1
    Attribute.invertColorTable = 1

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
