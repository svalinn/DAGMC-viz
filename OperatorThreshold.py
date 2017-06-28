from visit import *


def OperatorThreshold(OperSet, myList, tags):
    """
    expr = tagname > val | tagname < val | tagname = (min,max)
    """

    SetActivePlots(tags[myList[0]])
    AddOperator(OperSet, 0)

    if myList is not None:
        myList = list(myList)

        Attribute = ThresholdAttributes()

        if myList[1] == "=":
            Attribute.lowerBounds = myList[2][0]
            Attribute.upperBounds = myList[2][1]

        if myList[1] == ">":
            Attribute.lowerBounds = myList[2]

        if myList[1] == "<":
            Attribute.upperBounds = myList[2]

        SetOperatorOptions(Attribute)
