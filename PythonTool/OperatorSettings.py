from visit import *

from Operators import *


class OperatorSettings(object):
    """Add operator and its settings."""

    def __init__(
                 self,
                 File,
                 OperSet,
                 OperOptions,
                 Centroids,
                 tags,
                 PlottingSpatialExtents,
                 SliceProject=1
                 ):

        self.File = File
        self.tags = tags
        self.OperSet = OperSet
        self.Centroids = Centroids
        self.OperOptions = OperOptions
        self.SliceProject = SliceProject
        self.PlottingSpatialExtents = PlottingSpatialExtents

    def Slice(self):
        OperatorSlice(
                      self.File,
                      self.OperSet,
                      self.OperOptions,
                      self.Centroids,
                      self.PlottingSpatialExtents,
                      self.SliceProject,
                      )

    def Clip(self):
        OperatorClip(
                     self.File,
                     self.OperSet,
                     self.OperOptions,
                     self.Centroids,
                     )

    def Threshold(self):
        OperatorThreshold(
                          self.OperSet,
                          self.OperOptions,
                          self.tags,
                          )

    def Transform(self):
        OperatorTransform(
                          self.File,
                          self.OperSet,
                          self.OperOptions,
                          self.Centroids,
                          )
