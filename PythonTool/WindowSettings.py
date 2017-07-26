import os

from visit import *


def WindowSettings(Shading=False):
    """Modify window settings."""

    # Set window attributes for saving.
    MoveAndResizeWindow(1, 0, 0, 2048, 1024)

    Attribute = SaveWindowAttributes()

    Attribute.format = Attribute.PNG

    Attribute.fileName = "../Images/sample"

    SetSaveWindowAttributes(Attribute)

    # Set lighting attributes.
    if Shading is False:
        light = GetLight(0)
        light.type = light.Ambient
        SetLight(0, light)
    else:
        pass

    # Change annotation options
    Annotation = AnnotationAttributes()

    Scale = 1.5
        
    Annotation.axes3D.xAxis.label.font.scale = Scale
    Annotation.axes3D.yAxis.label.font.scale = Scale
    Annotation.axes3D.zAxis.label.font.scale = Scale

    Annotation.axes2D.xAxis.label.font.scale = Scale
    Annotation.axes2D.yAxis.label.font.scale = Scale

    Annotation.axes3D.xAxis.label.font.bold = 1
    Annotation.axes3D.yAxis.label.font.bold = 1
    Annotation.axes3D.zAxis.label.font.bold = 1

    Annotation.axes2D.xAxis.label.font.bold = 1
    Annotation.axes2D.yAxis.label.font.bold = 1

    Annotation.legendInfoFlag = 1
    Annotation.databaseInfoFlag = 0
    Annotation.timeInfoFlag = 0
    Annotation.userInfoFlag = 0

    SetAnnotationAttributes(Annotation)
