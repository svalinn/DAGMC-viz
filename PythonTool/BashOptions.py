import subprocess
import ast


class BashOptions(object):
    """Bash execution options."""

    def __init__(self, Options):
        self.Options0 = ast.literal_eval(Options)[0]
        self.Options1 = ast.literal_eval(Options)[1]

        try:
            self.Options2 = ast.literal_eval(Options)[2]
        except Exception:
            pass

    def DataConvert(self):
        """Use mbconvert for data conversion."""

        subprocess.call([
                         "bash",
                         "../BashTool/DataConvert.sh",
                         str(self.Options0),
                         str(self.Options1),
                         ])

    def GraveRemove(self):
        """Export an stl file without a graveyard."""

        subprocess.call([
                         "bash",
                         "../BashTool/GraveRemove.sh",
                         str(self.Options0),
                         str(self.Options1),
                         ])

    def SurfacesNoGrave(self):
        """Export surfaces (stl) without a graveyard."""

        subprocess.call([
                         "bash",
                         "../BashTool/SurfacesNoGrave.sh",
                         str(self.Options0),
                         str(self.Options1),
                         ])

    def CurvesNoGrave(self):
        """Export curves (vtk) without a graveyard."""

        subprocess.call([
                         "bash",
                         "../BashTool/CurvesNoGrave.sh",
                         str(self.Options0),
                         str(self.Options1),
                         ])

    def SessionReplaceSingle(self):
        """Replace one loaded data source within a single session."""

        subprocess.call([
                         "bash",
                         "../BashTool/SessionReplaceSingle.sh",
                         str(self.Options0),
                         str(self.Options1),
                         str(self.Options2),
                         ])

    def SessionReplaceMultiple(self):
        """Replace one loaded data source within all sessions."""

        subprocess.call([
                         "bash",
                         "../BashTool/SessionReplaceMultiple.sh",
                         str(self.Options0),
                         str(self.Options1),
                         ])
