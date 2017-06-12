from visit import *

Coordinates = [str(0)]

def OperatorSettings():
    """Add operator and it's settings."""

    # Non automated way of determining where I should crop the plots.
    DrawPlots()
    Query("SpatialExtents")
    #Coordinates.append([str(GetQueryOutputValue())])
    #print(Coordinates)

    # Coordinates = (-49.5, 49.5, -14.1, 77.43, -49.2, 49.2)
    Attribute = BoxAttributes()

    Attribute.minx = -49.5# Coordinates[0]
    Attribute.maxx = 49.5# Coordinates[1]

    Attribute.miny = -14.1# Coordinates[2]
    Attribute.maxy = 77.43# Coordinates[3]

    Attribute.minz = -49.2# Coordinates[4]
    Attribute.maxz = 49.2# Coordinates[5]

    SetOperatorOptions(Attribute)

    Attribute = SliceAttributes()

    Attribute.axisType = Attribute.YAxis

    SetOperatorOptions(Attribute)
