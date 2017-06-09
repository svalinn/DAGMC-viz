from visit import *


def Save():
    """Displays plots on windows and saves sessions and images."""

    DrawPlots()
    SaveSession("./Sessions/XML/example.session")
    WriteScript(open("./Sessions/Python/example.py", "wt"))
    SaveWindow()
