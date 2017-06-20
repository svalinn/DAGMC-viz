import os

from visit import *


def SaveSessions():
    """This saves Python and XML session files in an incremental way."""

    i = 0
    while os.path.exists("./Sessions/XML/Original/sample%s.session" % i):
        i += 1

    SaveSession("./Sessions/XML/Original/sample%s.session" % i)

    # VisIt 2.12.2 documentation states that the python session
    # is not completed.

    i = 0
    while os.path.exists("./Sessions/Python/sample%s.py" % i):
        i += 1

    WriteScript(open("./Sessions/Python/sample{}.py".format(i), "wt"))
