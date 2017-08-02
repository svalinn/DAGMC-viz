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

        # Load the plots without operators.
        for item in Files:
            Vi.SetActiveWindow(Count)  # Select window to be worked in.
            Image = Mk.MakeImages([item])
            Image.Plot()
            Image.Save()
            Vi.ToggleLockViewMode()  # Lock the view perspective.
            Vi.AddWindow()  # Add another window for next iteration.
            Count += 1

        try:
            # Display plots with operators if defined.
            for item in OperatorSet:
                Vi.SetActiveWindow(Count)  # Select window to be worked in.
                It.Iterator(Files, [item], SliceProject=0)
                Vi.DrawPlots()  # Draw plots with operator.
                Wi.WindowSettings()
                Vi.ToggleLockViewMode()  # Lock the view perspective.
                Vi.AddWindow()  # Add another window for next iteration.
                Count += 1

        except Exception:
            pass

        # Last window is always empty.
        Vi.SetActiveWindow(Count)
        Vi.DeleteWindow()  # Delete last window.

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

        # Alternate saving scheme for multiple windows is used.
        i = 0
        while os.path.exists(
                             "../Sessions/XML_Original/sampleMulti%s.session"
                             % i
                             ):
            i += 1

        Vi.SaveSession("../Sessions/XML_Original/sampleMulti%s.session" % i)
