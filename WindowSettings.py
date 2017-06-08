from visit import *

def WindowSettings():
	"""Modify window settings."""

	Attribute = SaveWindowAttributes()
	Attribute.format = Attribute.BMP
	Attribute.fileName = "./Images/example"
	Attribute.width = 2000
	Attribute.height = 2000
	Attribute.screenCapture = 0

	SetSaveWindowAttributes(Attribute)
