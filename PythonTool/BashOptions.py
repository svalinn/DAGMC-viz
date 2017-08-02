import subprocess
import ast


class BashOptions(object):
    """Bash execution options."""

    def __init__(self, Options):
        self.Options = Options

    def DataConvert(self):
        FileIn = ast.literal_eval(self.Options)[0]
        FileOut = ast.literal_eval(self.Options)[1]

        subprocess.call([
                         "bash",
                         "../BashTool/DataConvert.sh",
                         str(FileIn),
                         str(FileOut),
                         ])

    def GraveRemove(self):
        h5mFile = ast.literal_eval(self.Options)[0]
        stlFile = ast.literal_eval(self.Options)[1]

        subprocess.call([
                         "bash",
                         "../BashTool/GraveRemove.sh",
                         str(h5mFile),
                         str(stlFile),
                         ])

    def Surfaces(self):
        h5mFile = ast.literal_eval(self.Options)[0]
        stlFile = ast.literal_eval(self.Options)[1]

        subprocess.call([
                         "bash",
                         "../BashTool/SurfacesNoGrave.sh",
                         str(h5mFile),
                         str(stlFile),
                         ])

    def Curves(self):
        h5mFile = ast.literal_eval(self.Options)[0]
        vtkFile = ast.literal_eval(self.Options)[1]

        subprocess.call([
                         "bash",
                         "../BashTool/CurvesNoGrave.sh",
                         str(h5mFile),
                         str(vtkFile),
                         ])

    def SessionReplaceSingle(self):
        SessionFile = ast.literal_eval(self.Options)[0]
        stlOld = ast.literal_eval(self.Options)[1]
        stlNew = ast.literal_eval(self.Options)[2]

        subprocess.call([
                         "bash",
                         "../BashTool/SessionReplaceSingle.sh",
                         str(SessionFile),
                         str(stlOld),
                         str(stlNew),
                         ])

    def SessionReplaceMultiple(self):
        stlOld = ast.literal_eval(self.Options)[0]
        stlNew = ast.literal_eval(self.Options)[1]

        subprocess.call([
                         "bash",
                         "../BashTool/SessionReplaceMultiple.sh",
                         str(stlOld),
                         str(stlNew),
                         ])
