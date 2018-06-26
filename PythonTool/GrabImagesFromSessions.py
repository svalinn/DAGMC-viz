import os

import visit as Vi

try:
    Vi.Launch()  # Here to allow import of other modules.
except Exception:
    pass


def GrabImagesFromSessions():
    """
    A function that loads session files
    and grabs images from it.
    """

    Directory = str(os.getcwd())+"/../Sessions/XML_Edited"

    for file in sorted(os.listdir(Directory)):
        if file.endswith(".session"):

            # Find each session file and restore it in VisIt
            Vi.RestoreSession(os.path.join(Directory, file), 0)

            # Save directory defined by session.
            Vi.SaveWindow()
