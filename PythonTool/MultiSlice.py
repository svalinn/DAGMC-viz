import math as Ma

import visit as Vi

import PathCreator as Pa
import MakeImagesPython as Mk


def MultiSlice(File, myList):
    """
    Take multiple sliced along an axis.
    Slices are evenly spaced.
    myList = (<axis>, <number of slices>).
    """

    Pa.PathCreator()  # Creates necessary folders.

    myList = list(myList)

    Image = Mk.MakeImages(File)
    Image.Plot()
    Bounds = Image.get_list()[2]

    xLower = Bounds["Pseudocolor"][0]
    xUpper = Bounds["Pseudocolor"][1]

    yLower = Bounds["Pseudocolor"][2]
    yUpper = Bounds["Pseudocolor"][3]

    zLower = Bounds["Pseudocolor"][4]
    zUpper = Bounds["Pseudocolor"][5]

    xRange = xUpper-xLower
    yRange = yUpper-yLower
    zRange = zUpper-zLower

    Number = int(myList[1])

    xIncrement = xRange/float(Number)
    yIncrement = yRange/float(Number)
    zIncrement = zRange/float(Number)

    for i in range(len(myList[0])):
        Axis = myList[0][i]

        # For adding slices of and between maximum and minimum dimensions.
        Count = 0
        SliceList = []
        for i in range(Number):

            # Round up for lower bound.
            if Count == 0:
                Lower = Ma.ceil(eval(Axis.lower()+"Lower"))
                SliceSet = Ma.floor(eval(Axis.lower()+"Increment"))*Count
                SliceList.append([
                                  "Slice",
                                  (Axis.lower(), Lower+SliceSet)
                                 ])
            # Round down for upper bound.
            elif Count == Number-1:
                Lower = eval(Axis.lower()+"Lower")
                SliceSet = Ma.floor(eval(Axis.lower()+"Increment"))*Count
                SliceList.append([
                                  "Slice",
                                  (Axis.lower(), Lower+SliceSet)
                                 ])
            else:
                Lower = eval(Axis.lower()+"Lower")
                SliceSet = eval(Axis.lower()+"Increment")*Count
                SliceList.append([
                                  "Slice",
                                  (Axis.lower(), Lower+SliceSet)
                                 ])
            Count += 1

        for item in SliceList:
            Operator = item[0]
            List = item[1]
            Vi.RemoveAllOperators(all)  # Removes previous slice in loop.
            Image.Operator(Operator, List)
            Image.Save()
