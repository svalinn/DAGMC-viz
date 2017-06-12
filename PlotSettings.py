from visit import *


def PlotSettings():
    """Visual settings for plots."""

    # Pseudocolor plot attributes.
    Attribute = PseudocolorAttributes()

    Attribute.lineStyle = Attribute.DASH
    Attribute.scaling = Attribute.Linear
    Attribute.centering = Attribute.Nodal

    SetPlotOptions(Attribute)

    # Mesh plot attributes.
    Attribute = MeshAttributes()

    Attribute.lineStyle = Attribute.DASH

    SetPlotOptions(Attribute)

    # Contour plot attributes.
    Attribute = ContourAttributes()

    Attribute.lineStyle = Attribute.DASH

    SetPlotOptions(Attribute)
