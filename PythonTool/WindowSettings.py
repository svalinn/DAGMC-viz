import os

from visit import *


def WindowSettings(Shading=False):
    """Modify window settings."""

    # Set window attributes for saving.
    MoveAndResizeWindow(1, 0, 0, 2048, 1024)

    Attribute = SaveWindowAttributes()  # Enables changing window attributes.

    Attribute.format = Attribute.PNG  # Make image a PNG.

    Attribute.fileName = "../Images/sample"  # Set image name.

    SetSaveWindowAttributes(Attribute)  # Apply changed attributes.

    # Set lighting attributes.
    if Shading is False:
        light = GetLight(0)
        light.type = light.Ambient
        SetLight(0, light)
    else:
        pass

    # Change annotation options
    Annotation = AnnotationAttributes()

    # Set the scale of the font of each axis.
    Scale = 1.5

    Annotation.axes3D.xAxis.label.font.scale = Scale
    Annotation.axes3D.yAxis.label.font.scale = Scale
    Annotation.axes3D.zAxis.label.font.scale = Scale

    Annotation.axes2D.xAxis.label.font.scale = Scale
    Annotation.axes2D.yAxis.label.font.scale = Scale

    # Make font bold for axes.
    Annotation.axes3D.xAxis.label.font.bold = 1
    Annotation.axes3D.yAxis.label.font.bold = 1
    Annotation.axes3D.zAxis.label.font.bold = 1

    Annotation.axes2D.xAxis.label.font.bold = 1
    Annotation.axes2D.yAxis.label.font.bold = 1

    # Reduced the information displayed on a window.
    Annotation.legendInfoFlag = 1  # Controls legend display.
    Annotation.databaseInfoFlag = 0  # Controls data file name display.
    Annotation.timeInfoFlag = 0  # Controls time display.
    Annotation.userInfoFlag = 0  # Controls legend user information display.

    SetAnnotationAttributes(Annotation)
