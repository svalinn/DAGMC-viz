from visit import *


def PlotMesh(File):
    # Mesh plot attributes.

    if File is not None:
        File = dict(File)

        Attribute = MeshAttributes()

        for key in File:
            if File[key][1].title() == "Mesh":
                try:
                    Attribute.lineStyle = eval(
                                               "Attribute." +
                                               str(File[key][3]).upper()
                                               )
                except Exception:
                    pass

        SetPlotOptions(Attribute)
