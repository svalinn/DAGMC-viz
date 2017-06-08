from visit import *

def DataLoading(File):
	"""Load data to VisIt and add plot.


	Data used:
	*.vtk -- results
	*.stl -- geometry
	"""
	
	for key in File:
		OpenDatabase("./Data/"+key)
		AddPlot(File[key][0], File[key][1])
