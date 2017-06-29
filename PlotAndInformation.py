from visit import *


def PlotAndInformation(File):
    """Plot and find information regarding plots."""

    Count = 0
    PlotType = []
    Centroids = []
    plotnumber = []

    for item in File:
        OpenDatabase("./Data/"+item[0])
        AddPlot(item[1].title(), item[2])

        PlotType.append(item[1].title())
        plotnumber.append(Count)  # Loading order.

        SetActivePlots(Count)
        DrawPlots()

        Query("Centroid")  # Centroid of selected plot.
        Centroids.append(GetQueryOutputValue())

        Count += 1

    # Create dictionaries of plot information.
    PlottingSequence = dict(zip(PlotType, plotnumber))
    PlottingCentroids = dict(zip(PlotType, Centroids))

    return PlottingSequence, PlottingCentroids
