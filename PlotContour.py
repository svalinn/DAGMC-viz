from visit import *


def PlotContour(File):
    # Contour plot attributes.

    if File is not None:
        File = dict(File)

        Attribute = ContourAttributes()

        for key in File:
            if File[key][1].title() == "Contour":

                # Check for optional inputs in Dictionary input.
                try:
                    Attribute.lineStyle = eval(
                                               "Attribute." +
                                               str(File[key][3]).upper()
                                               )
                except Exception:
                    pass

        SetPlotOptions(Attribute)
