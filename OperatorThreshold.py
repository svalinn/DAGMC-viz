from visit import *


def OperatorThreshold(myList, tags):
    """
    expr = tagname > val | tagname < val | tagname = (min,max)
    """

    if myList is not None:
        myList = list(myList)

        SetActivePlots(tags[myList[0]])

        Attribute = ThresholdAttributes()

        if myList[1] == "=":
            Attribute.lowerBounds = myList[2][0]
            Attribute.upperBounds = myList[2][1]

        if myList[1] == ">":
            Attribute.lowerBounds = myList[2]

        if myList[1] == "<":
            Attribute.upperBounds = myList[2]

        SetOperatorOptions(Attribute)
