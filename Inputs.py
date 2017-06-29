# Key items are as follows:
# 1) The file containing data
# 2) A valid plot type
# 3) The variable plotted
# Keys are arbitrary.
Files = {
        "Plot_1": ["dummy.vtk", "Pseudocolor", "TALLY_TAG", "Log", 0.00001, 0.0001],
        "Plot_2": ["dummy.vtk", "Contour", "ERROR_TAG", "DASH"],
        #"Plot_3": ["dummy.stl", "Mesh", "STL_mesh", "DASH"],
        }

Operators = [
             {"Clip": {"oct": (1, 1, 1), "rot": (30, 30, 30), "loc":(0,0,0)}},
             ['Slice', ['x', 10]],
             ['Threshold', ['Pseudocolor', "=", (5.14*10**-05,0.00011)]],
             ['threshold', ['contour', "=", (0.0004614,0.0008)]],
             [{"Clip": {"oct": (1, 1, 1)}}, ['Slice', ['x', 10]],{"Clip": {"oct": (-1, -1, -1)}}]
             ]
