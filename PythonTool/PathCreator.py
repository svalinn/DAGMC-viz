import os


def PathCreator():
    """Form folders to contain Data, Sessions, and Images.


    Folders created:
    ../Images -- windows images saved
    ../Sessions/XML_Original -- XML session files
    ../Sessions/XML_Edited -- XML session files that were edited
    """

    if not os.path.exists("../Images"):
        os.makedirs("../Images")

    if not os.path.exists("../Sessions/XML_Edited"):
        os.makedirs("../Sessions/XML_Edited")

    if not os.path.exists("../Sessions/XML_Original"):
        os.makedirs("../Sessions/XML_Original")
