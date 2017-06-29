# Key items are as follows:
# 1) The file containing data
# 2) A valid plot type
# 3) The variable plotted
# Keys are arbitrary.
Files = {
        "Plot_1": ["dummy.vtk", "Pseudocolor", "TALLY_TAG", "Log"],
        "Plot_2": ["dummy.vtk", "Contour", "ERROR_TAG", "DASH"],
        "Plot_3": ["dummy.stl", "Mesh", "STL_mesh", "DASH"],
        }

Operators = [
             {"Clip": {"oct": (1, 1, 1)}},
             {"Clip": {"oct": (1, 1, 1), "rot": (30, 30, 30)}},
             ]
