from visit import *

def PlotSettings():
	"""Visual settings for plots."""

	# Pseudocolor plot attributes.
	Attribute = PseudocolorAttributes()

	Attribute.scaling = Attribute.Linear  # Linear Log Skew
	Attribute.skewFactor = 1
	Attribute.limitsMode = Attribute.OriginalData  # OriginalData CurrentPlot
	Attribute.minFlag = 0
	Attribute.min = 0
	Attribute.maxFlag = 0
	Attribute.max = 1
	Attribute.centering = Attribute.Natural # Natural Nodal Zonal
	Attribute.colorTableName = "hot"  # See options in VisIt
	Attribute.invertColorTable = 0
	Attribute.opacityType = Attribute.FullyOpaque  # FullyOpaque ColorTable Constant Ramp VariableRange
	Attribute.opacityVariable = ""
	Attribute.opacity = 1
	Attribute.opacityVarMin = 0
	Attribute.opacityVarMax = 1
	Attribute.opacityVarMinFlag = 0
	Attribute.opacityVarMaxFlag = 0
	Attribute.pointSize = 0.05
	Attribute.pointType = Attribute.Point  # Point Box Axis Icosahedron Octahedron Tetrahedron SphereGeometry Point Sphere
	Attribute.pointSizeVarEnabled = 0
	Attribute.pointSizeVar = "default"
	Attribute.pointSizePixels = 2
	Attribute.lineType = Attribute.Tube  # Line Tube Ribbon
	Attribute.lineStyle = Attribute.SOLID  # SOLID DASH DOT DOTDASH
	Attribute.lineWidth = 0
	#Attribute.tubeDisplayDensity = 10
	Attribute.tubeRadiusSizeType = Attribute.FractionOfBBox  # FractionOfBBox Absolute
	Attribute.tubeRadiusAbsolute = 0.125
	Attribute.tubeRadiusBBox = 0.005
	#Attribute.varyTubeRadius = 0
	#Attribute.varyTubeRadiusVarible = ""
	#Attribute.varyTubeRadiusFactor = 10
	#Attribute.endPointType = Attribute.None  # None Tails Heads Both
	#Attribute.endPointStyle = Attribute.Spheres  # Spheres Cones
	Attribute.endPointRadiusSizeType = Attribute.FractionOfBBox # FractionOfBBox Absolute
	Attribute.endPointRadiusAbsolute = 1
	Attribute.endPointRadiusBBox = 0.005
	Attribute.endPointRatio = 2
	Attribute.renderSurfaces = 1
	Attribute.renderWireframe = 0
	Attribute.renderPoints = 0
	Attribute.smoothingLevel = 0
	Attribute.legendFlag = 1
	Attribute.lightingFlag = 1

	SetPlotOptions(Attribute)


	# Mesh plot attributes.
	Attribute = MeshAttributes()

	Attribute.legendFlag = 1
	Attribute.lineStyle = Attribute.SOLID  # SOLID DASH DOT DOTDASH
	Attribute.lineWidth = 0
	Attribute.meshColor = (0, 0, 0, 255)
	Attribute.meshColorSource = Attribute.Foreground  # Foreground MeshCustom
	Attribute.opaqueColorSource = Attribute.Background  # Background OpaqueCustom
	Attribute.opaqueMode = Attribute.Auto  # Auto On Off
	Attribute.pointSize = 0.05
	Attribute.opaqueColor = (255, 255, 255, 255)
	Attribute.smoothingLevel = Attribute.None  # None Fast High
	Attribute.pointSizeVarEnabled = 0
	Attribute.pointSizeVar = "default"
	Attribute.pointType = Attribute.Point  # Point Box Axis Icosahedron Octahedron Tetrahedron SphereGeometry Point Sphere
	Attribute.showInternal = 0
	Attribute.pointSizePixels = 2
	Attribute.opacity = 1

	SetPlotOptions(Attribute)
