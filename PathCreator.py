import os


def PathCreator():
    """Form folders to contain Data, Sessions, and Images.


    Folders created:
    ./Images -- windows images saved
    ./Sessions/Python -- python session files
    ./Sessions/XML/Original -- XML session files
    ./Sessions/XML/Edited -- XML session files that were edited
    """

    if not os.path.exists("./Images"):
        os.makedirs("./Images")

    if not os.path.exists("./Sessions/Python"):
        os.makedirs("./Sessions/Python")

    if not os.path.exists("./Sessions/XML/Edited"):
        os.makedirs("./Sessions/XML/Edited")

    if not os.path.exists("./Sessions/XML/Original"):
        os.makedirs("./Sessions/XML/Original")
