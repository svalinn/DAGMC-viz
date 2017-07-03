import visit as Vi

import PathCreator as Pa
import Iterator as It
import MakeImagesPython as Mk


def MultipleWindows(Files, OperatorSet=None):
    """
    Attain:
    pseudo color of tally,
    contour of error,
    XY slice, YZ slice, ZX slice,
    Clip quadrant 1 at center.
    """

    Pa.PathCreator()  # Creates necessary folders.
    Image = Mk.MakeImages(Files)
    Image.Plot()

    print Image.get_list()[0]
    print Image.get_list()[1]

    Count = 2
    for item in Files:
        print Count
        Vi.AddWindow()
        Vi.SetActiveWindow(Count)
        Vi.AddPlot(item[1].title(), item[2])
        Vi.DrawPlots()
        Count += 1

    for item in OperatorSet:
        Vi.AddWindow()
        Vi.SetActiveWindow(Count)
        print item
        It.Iterator(Files, [item])
        Vi.DrawPlots()
        Count += 1

    Vi.ToggleLockViewMode()
