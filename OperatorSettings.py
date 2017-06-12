from visit import *

def OperatorSettings():
    """Add operator and it's settings."""

    Attribute = SliceAttributes()

    # # Intercept Point Intercept Percent Zone Node
    # Attribute.originType = Attribute.Intercept
    # Attribute.originPoint = (0, 0, 0)
    # Attribute.originIntercept = 0
    # Attribute.originPercent = 0
    # Attribute.originZone = 0
    # Attribute.originNode = 0
    # Attribute.normal = (0, -1, 0)
    # # XAxis YAxis ZAxis Arbitrary ThetaPhi
    Attribute.axisType = Attribute.ZAxis
    # Attribute.upAxis = (0, 0, 1)
    # Attribute.project2d = 1
    # Attribute.interactive = 1
    # Attribute.flip = 0
    # Attribute.originZoneDomain = 0
    # Attribute.originNodeDomain = 0
    # Attribute.meshName = "default"
    # Attribute.theta = 0
    # Attribute.phi = 0

    SetOperatorOptions(Attribute)
