import os

import visit as Vi

import Iterator as It
import PathCreator as Pa
import WindowSettings as Wi
import MakeImagesPython as Mk


def MultipleWindows(Files, OperatorSet=None, Windows=False, SliceProject=1):
    """
    Attain multiple windows for different applied operators.
    Data other than mesh are plotted individually as well.
    """

    if Windows is False:
        It.Iterator(Files, OperatorSet)

    if Windows is True:
        Pa.PathCreator()  # Creates necessary folders.

        Count = 1
        for item in Files:
            Vi.SetActiveWindow(Count)
            Image = Mk.MakeImages([item])
            Image.Plot()
            Image.Save()
            Vi.ToggleLockViewMode()
            Vi.AddWindow()
            Count += 1

        try:
            for item in OperatorSet:
                Vi.SetActiveWindow(Count)
                It.Iterator(Files, [item], SliceProject=0)
                Vi.DrawPlots()
                Wi.WindowSettings()
                Vi.ToggleLockViewMode()
                Vi.AddWindow()
                Count += 1

        except Exception:
            pass

        Vi.SetActiveWindow(Count)
        Vi.DeleteWindow()  # Delete extra window.

        # Compensate for odd number of windows.
        if (Count-1) < 2:
            Vi.SetWindowLayout(1)
        elif (Count-1) == 2:
            Vi.SetWindowLayout(2)
        elif 2 < (Count-1) <= 4:
            Vi.SetWindowLayout(4)
        elif 4 < (Count-1) <= 6:
            Vi.SetWindowLayout(6)
        elif 6 < (Count-1) <= 8:
            Vi.SetWindowLayout(8)
        elif (Count-1) == 9:
            Vi.SetWindowLayout(9)
        elif 9 > (Count-1) <= 16:
            print "Too many windows to view nicely."
        else:
            print "Too many windows for ViSit to Support."

        i = 0
        while os.path.exists(
                             "../Sessions/XML_Original/SampleMulti%s.session"
                             % i
                             ):
            i += 1

        Vi.SaveSession("../Sessions/XML_Original/SampleMulti%s.session" % i)
