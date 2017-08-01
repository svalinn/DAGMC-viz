from visit import *


def OperatorThreshold(OperSet, OperOptions, tags):
    """
    expr = plottype > val | plottype < val | plottype = (min,max)
    """

    ResetView()
    SetActivePlots(tags[OperOptions[0].title()])
    AddOperator(OperSet.title(), 0)

    if OperOptions is not None:
        OperOptions = list(OperOptions)
        Bounds = eval(OperOptions[2])

        Attribute = ThresholdAttributes()

        if OperOptions[1] == "=":
            Attribute.lowerBounds = Bounds[0]
            Attribute.upperBounds = Bounds[1]

        if OperOptions[1] == ">":
            Attribute.lowerBounds = Bounds

        if OperOptions[1] == "<":
            Attribute.upperBounds = Bounds

        SetOperatorOptions(Attribute)
