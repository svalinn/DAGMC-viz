import visit

import PathCreator
import DataLoading
import PlotSettings
import OperatorSettings
import WindowSettings
import Saving

# Files here is temporary
Files = {
    "meshtal.vtk": ["Pseudocolor"]+["TALLY_TAG"],
    "fng_zip.stl": ["Mesh"]+["STL_mesh"],
    }

visit.LaunchNowin()
PathCreator.PathCreator()
DataLoading.DataLoading(Files)
PlotSettings.PlotSettings()
OperatorSettings.OperatorSettings()
WindowSettings.WindowSettings()
Saving.Saving()
