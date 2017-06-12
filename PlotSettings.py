from visit import *


def PlotSettings():
    """Visual settings for plots."""

    # Pseudocolor plot attributes.
    Attribute = PseudocolorAttributes()


    Attribute.scaling = Attribute.Log

    # # Linear Log Skew
    # Attribute.scaling = Attribute.Linear
    # Attribute.skewFactor = 1
    # # OriginalData CurrentPlot
    # Attribute.limitsMode = Attribute.OriginalData
    # Attribute.minFlag = 0
    # Attribute.min = 0
    # Attribute.maxFlag = 0
    # Attribute.max = 1
    # # Natural Nodal Zonal
    # Attribute.centering = Attribute.Natural
    # # See options in VisIt
    # Attribute.colorTableName = "hot"
    # Attribute.invertColorTable = 0
    # # FullyOpaque ColorTable Constant Ramp VariableRange
    # Attribute.opacityType = Attribute.FullyOpaque
    # Attribute.opacityVariable = ""
    # Attribute.opacity = 1
    # Attribute.opacityVarMin = 0
    # Attribute.opacityVarMax = 1
    # Attribute.opacityVarMinFlag = 0
    # Attribute.opacityVarMaxFlag = 0
    # Attribute.pointSize = 0.05
    # # Point Box Axis Icosahedron Octahedron Tetrahedron SphereGeometry Point Sphere
    # Attribute.pointType = Attribute.Point
    # Attribute.pointSizeVarEnabled = 0
    # Attribute.pointSizeVar = "default"
    # Attribute.pointSizePixels = 2
    # # Line Tube Ribbon
    # Attribute.lineType = Attribute.Tube
    # # SOLID DASH DOT DOTDASH
    # Attribute.lineStyle = Attribute.SOLID
    # Attribute.lineWidth = 0
    # # The following does not work: Attribute.tubeDisplayDensity = 10


    # # The following three do not work without an operator:
    # # FractionOfBBox Absolute
    # # Attribute.tubeRadiusSizeType = Attribute.FractionOfBBox
    # # Attribute.tubeRadiusAbsolute = 0.125
    # # Attribute.tubeRadiusBBox = 0.005


    # # The following does not work: Attribute.varyTubeRadius = 0
    # # The following does not work: Attribute.varyTubeRadiusVarible = ""
    # # The following does not work: Attribute.varyTubeRadiusFactor = 10
    # # The following does not work: Attribute.endPointType = Attribute.None  # None Tails Heads Both
    # # The following does not work: Attribute.endPointStyle = Attribute.Spheres  # Spheres Cones
    # # FractionOfBBox Absolute
    # Attribute.endPointRadiusSizeType = Attribute.FractionOfBBox
    # Attribute.endPointRadiusAbsolute = 1
    # Attribute.endPointRadiusBBox = 0.005
    # Attribute.endPointRatio = 2
    # Attribute.renderSurfaces = 1
    # Attribute.renderWireframe = 0
    # Attribute.renderPoints = 0
    # Attribute.smoothingLevel = 0
    # Attribute.legendFlag = 1
    # Attribute.lightingFlag = 1

    SetPlotOptions(Attribute)

    # # Mesh plot attributes.
    # Attribute = MeshAttributes()

    # Attribute.legendFlag = 1
    # Attribute.lineStyle = Attribute.SOLID  # SOLID DASH DOT DOTDASH
    # Attribute.lineWidth = 0
    # Attribute.meshColor = (0, 0, 0, 255)
    # Attribute.meshColorSource = Attribute.Foreground  # Foreground MeshCustom
    # Attribute.opaqueColorSource = Attribute.Background  # Background OpaqueCustom
    # Attribute.opaqueMode = Attribute.Auto  # Auto On Off
    # Attribute.pointSize = 0.05
    # Attribute.opaqueColor = (255, 255, 255, 255)
    # Attribute.smoothingLevel = Attribute.None  # None Fast High
    # Attribute.pointSizeVarEnabled = 0
    # Attribute.pointSizeVar = "default"
    # Attribute.pointType = Attribute.Point  # Point Box Axis Icosahedron Octahedron Tetrahedron SphereGeometry Point Sphere
    # Attribute.showInternal = 0
    # Attribute.pointSizePixels = 2
    # Attribute.opacity = 1

    # SetPlotOptions(Attribute)
