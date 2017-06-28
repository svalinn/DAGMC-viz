from visit import *


def PlotPseudocolor(File):
    # Pseudocolor plot attributes.

    if File is not None:
        File = dict(File)

        Attribute = PseudocolorAttributes()

        for key in File:
            if File[key][1].title() == "Pseudocolor":
                try:
                    Attribute.scaling = eval(
                                             "Attribute." +
                                             str(File[key][3]).title()
                                             )
                except Exception:
                    pass

                try:
                    Attribute.min = File[key][4]
                    Attribute.minFlag = 1
                except Exception:
                    pass

                try:
                    Attribute.max = File[key][5]
                    Attribute.maxFlag = 1
                except Exception:
                    pass

        SetPlotOptions(Attribute)
