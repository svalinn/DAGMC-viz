import os

from visit import *


def SaveSessions():
    """This saves XML session files in an incremental way."""

    i = 0
    while os.path.exists("./Sessions/XML_Original/sample%s.session" % i):
        i += 1

    SaveSession("./Sessions/XML_Original/sample%s.session" % i)
