# Key items are as follows:
# 1) The file containing data
# 2) A valid plot type
# 3) The variable plotted
Files = {
    "Plot_1": ["dummy.vtk"]+["Pseudocolor"]+["TALLY_TAG"],
    "Plot_2": ["dummy.vtk"]+["Contour"]+["ERROR_TAG"],
    "Plot_3": ["dummy.stl"]+["Mesh"]+["STL_mesh"],
    }

# Key items are as follows:
# 1) Valid operator name
# 2) Apply to all (1) or not (0)
Operators = {
    "Operator_1": ["Clip"]+["1"],
    "Operator_2": ["Transform"]+["1"],
    }
