from visit import *


def OperatorSlice(File, OperSet, myList):
    """
    with no args - default direction and location
    [(<x,y,z>,val),(<x,y,z>,val),....]
    produces one image for each tuple with slice at plane <x,y,z>=val
    """

    AddOperator(OperSet, 1)
    SetActivePlots((tuple(range(0, len(File)))))

    if myList is not None:
        myList = list(myList)

        Attribute = SliceAttributes()

        Attribute.originType = Attribute.Point

        if myList[0].lower() == "x":
            Attribute.originPoint = (myList[1], 0, 0)

        if myList[0].lower() == "y":
            Attribute.originPoint = (0, myList[1], 0)

        if myList[0].lower() == "z":
            Attribute.originPoint = (0, 0, myList[1])

        Attribute.axisType = eval("Attribute."+str(myList[0]).upper()+"Axis")

        SetOperatorOptions(Attribute)
