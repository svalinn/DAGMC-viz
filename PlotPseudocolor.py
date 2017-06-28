from visit import *


def PlotPseudocolor(myList):
    # Pseudocolor plot attributes.

    if myList is not None:
        myList = list(myList)

        Attribute = PseudocolorAttributes()

        Attribute.scaling = eval("Attribute."+str(myList[0]).title())

        SetPlotOptions(Attribute)

