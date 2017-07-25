import os

from visit import *


def WindowSettings(Shading=False):
    """Modify window settings."""

    # Set window attributes for saving.
    MoveAndResizeWindow(1, 0, 0, 2048, 1024)


    Attribute = SaveWindowAttributes()

    Attribute.format = Attribute.PNG

    Attribute.fileName = "../Images/sample"

    Attribute.width = 1024
    Attribute.height = 1024

    SetSaveWindowAttributes(Attribute)

    # Set legend options.
    Attribute = AnnotationAttributes()

    Attribute.databaseInfoFlag = 0
    Attribute.legendInfoFlag = 1

    SetAnnotationAttributes(Attribute)

    # Set lighting attributes.
    if Shading is False:
        light = GetLight(0)
        light.type = light.Ambient
        SetLight(0, light)
    else:
        pass

    # Change legend options
    Attribute = AnnotationAttributes()

    Attribute.legendInfoFlag = 1
    Attribute.databaseInfoFlag = 0
    Attribute.timeInfoFlag = 0
    Attribute.userInfoFlag = 0


    SetAnnotationAttributes(Attribute)

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

    SetAnnotationAttributes(Annotation)
