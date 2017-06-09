import os


def PathCreator():
    """Form folders to contain Data, Sessions, and Images.


    Folders created:
    ./Images -- windows images saved
    ./Sessions/Python -- python session files
    ./Sessions/XML -- XML session files
    """

    if not os.path.exists("./Images"):
        os.makedirs("./Images")

    if not os.path.exists("./Sessions/Python"):
        os.makedirs("./Sessions/Python")

    if not os.path.exists("./Sessions/XML"):
        os.makedirs("./Sessions/XML")
