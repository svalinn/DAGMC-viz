import argparse
import ast

from visit import *

import MultipleWindows as Mw
import MultiSlice as Ms
import Orbit as Or


class TerminalOptions(object):
    """ Terminal execution settings."""

    def __init__(self, Arguments, FilePlots, OperatorSet=None):
        self.Arguments = Arguments
        self.FilePlots = FilePlots
        self.OperatorSet = OperatorSet

    def Images(self):
        try:
            Mw.MultipleWindows(self.FilePlots, self.OperatorSet, Windows=True)
        except Exception:
            Mw.MultipleWindows(self.FilePlots, Windows=True)

    def Windows(self):
        try:
            Mw.MultipleWindows(self.FilePlots, self.OperatorSet, Windows=True)
        except Exception:
            Mw.MultipleWindows(self.FilePlots, Windows=True)

    def Default(self):
        self.OperatorSet = [
                           ["Slice", ("x")],
                           ["Slice", ("y")],
                           ["Slice", ("z")],
                           [{"Clip": {"oct": (1, 1, 1)}}],
                           ]

        tic = timeit.default_timer()  # Start timer.
        Mw.MultipleWindows(self.FilePlots, self.OperatorSet, Windows=True)

    def MultiSlice(self):
        Axis = ast.literal_eval(self.Arguments.multislice)[0]
        Number = ast.literal_eval(self.Arguments.multislice)[1]
        myList = (str(Axis), int(Number))

        tic = timeit.default_timer()  # Start timer.
        Ms.MultiSlice(self.FilePlots, myList)

    def Orbit(self):
        Statement = ast.literal_eval(self.Arguments.orbit)[0]

        try:
            if self.OperatorSet is None:
                self.OperatorSet = False
        except Exception:
            pass

        Direction = ast.literal_eval(self.Arguments.orbit)[1]
        Iteration = ast.literal_eval(self.Arguments.orbit)[2]

        tic = timeit.default_timer()  # Start timer.
        Or.Orbit(self.FilePlots, (Direction, Iteration), self.OperatorSet)

    # def DataConvert(self):

    # def GraveRemove(self):

    # def Surfaces(sefl):

    # def Curves(self):

    # def SessionReplace(self):
