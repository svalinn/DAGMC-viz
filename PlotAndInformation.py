from visit import *


def PlotAndInformation(File):
    """Plot and find information regarding plots."""

    Count = 0
    PlotType = []
    Centroids = []
    plotnumber = []

    for key in File:
        OpenDatabase("./Data/"+File[key][0])
        AddPlot(File[key][1].title(), File[key][2])

        PlotType.append(File[key][1].title())
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
