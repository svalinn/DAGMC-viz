from visit import *


def PlotContour(File):
    # Contour plot attributes.

    if File is not None:
        File = list(File)

        Attribute = ContourAttributes()

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
