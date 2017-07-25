from visit import *


def PlotAndInformation(File):
    """Plot and find information regarding plots."""

    Count = 0
    PlotType = []
    Centroids = []
    plotnumber = []
    PlotObjects = []
    SpatialExtents = []

    for item in File:
        OpenDatabase("../Data/"+item[0])
        AddPlot(item[1].title(), item[2])

        PlotType.append(item[1].title())
        plotnumber.append(Count)  # Loading order.

        SetActivePlots(Count)
        DrawPlots()

        Query("Centroid")  # Centroid of selected plot.
        Centroids.append(GetQueryOutputValue())

        Query("SpatialExtents")  # Bounds of selected plot.
        SpatialExtents.append(GetQueryOutputValue())

        PlotObjects.append((GetAnnotationObjectNames())[Count])

        Count += 1

    # Create dictionaries of plot information.
    ObjectSequence = dict(zip(PlotType, PlotObjects))
    PlottingSequence = dict(zip(PlotType, plotnumber))
    PlottingCentroids = dict(zip(PlotType, Centroids))
    PlottingSpatialExtents = dict(zip(PlotType, SpatialExtents))

    return(
           PlottingSequence,
           PlottingCentroids,
           PlottingSpatialExtents,
           ObjectSequence,
           )
