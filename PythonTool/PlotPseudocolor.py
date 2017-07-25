from visit import *


def PlotPseudocolor(File, ObjectSequence):
    # Pseudocolor plot attributes.

    # Change orientation of legend
    LegendAttributes = GetAnnotationObject(ObjectSequence["Pseudocolor"])
    LegendAttributes.orientation = "VerticalLeft"
    LegendAttributes.fontHeight = 0.017

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
