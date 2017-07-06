from visit import *


def OperatorTransform(Files, OperSet, myList, Centroids):
    """
    Use rotation transform.
    (<Axis>, <Degree>)
    """

    ResetView()
    AddOperator(OperSet.title(), 1)
    SetActivePlots((tuple(range(0, len(Files)))))

    if myList is not None:
        myList = tuple(myList)
        print myList[0], myList[1]

        if myList[0].lower() == "x":
            Axis = (1, 0, 0)

        if myList[0].lower() == "y":
            Axis = (0, 1, 0)

        if myList[0].lower() == "z":
            Axis = (0, 0, 1)

        Attribute = TransformAttributes()

        Attribute.doRotate = 1

        Attribute.rotateAxis = Axis
        Attribute.rotateType = Attribute.Deg
        Attribute.rotateAmount = myList[1]

        try:
            Attribute.rotateOrigin = (
                                      Centroids["Pseudocolor"][0],
                                      Centroids["Pseudocolor"][1],
                                      Centroids["Pseudocolor"][2],
                                      )
        except Exception:
            pass

        SetOperatorOptions(Attribute)
