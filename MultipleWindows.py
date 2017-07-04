import visit as Vi

import PathCreator as Pa
import Iterator as It
import MakeImagesPython as Mk


def MultipleWindows(Files, OperatorSet=None, Windows=False):
    """
    Attain:
    pseudo color of tally,
    contour of error,
    XY slice, YZ slice, ZX slice,
    Clip quadrant 1 at center.
    """

    if Windows is False:
        It.Iterator(Files, OperatorSet)

    if Windows is True:
        Pa.PathCreator()  # Creates necessary folders.

        Count = 1
        for item in Files:
            if item[1] != "Mesh":
                Vi.SetActiveWindow(Count)
                Image = Mk.MakeImages([item])
                Image.Plot()
                Vi.DrawPlots()
                Vi.ToggleLockViewMode()
                Vi.AddWindow()
                Count += 1

            if item[1] == "Mesh":
                pass

        for item in OperatorSet:
            Vi.AddWindow()
            Vi.SetActiveWindow(Count)
            It.Iterator(Files, [item])
            Vi.DrawPlots()
            Vi.ToggleLockViewMode()
            Count += 1

        # Compensate for odd number of windows.
        if ((Count-1) % 2 == 0):
            Vi.SetWindowLayout(Count-1)  # Even.
        else:
            Vi.SetWindowLayout(Count)  # Odd.

        Image.Save()
