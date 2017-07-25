import os

import visit as Vi


def GrabImagesFromSessions():
    """
    A function that loads a session file
    and grabs images from it.
    """

    Directory = str(os.getcwd())+"/../Sessions/XML_Edited"

    for file in sorted(os.listdir(Directory)):
        if file.endswith(".session"):
            Vi.RestoreSession(os.path.join(Directory, file), 0)
            Vi.SaveWindow()
