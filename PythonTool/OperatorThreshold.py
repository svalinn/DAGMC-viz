from visit import *


def OperatorThreshold(OperSet, myList, tags):
    """
    expr = tagname > val | tagname < val | tagname = (min,max)
    """

    ResetView()
    SetActivePlots(tags[myList[0].title()])
    AddOperator(OperSet.title(), 0)

    if myList is not None:
        myList = list(myList)
        Bounds = eval(myList[2])

        Attribute = ThresholdAttributes()

        if myList[1] == "=":
            Attribute.lowerBounds = Bounds[0]
            Attribute.upperBounds = Bounds[1]

        if myList[1] == ">":
            Attribute.lowerBounds = Bounds

        if myList[1] == "<":
            Attribute.upperBounds = Bounds

        SetOperatorOptions(Attribute)
