from visit import *


def PlotPseudocolor():
    # Pseudocolor plot attributes.

    Attribute = PseudocolorAttributes()

    Attribute.lineStyle = Attribute.DASH
    Attribute.scaling = Attribute.Log
    Attribute.centering = Attribute.Nodal

    SetPlotOptions(Attribute)
