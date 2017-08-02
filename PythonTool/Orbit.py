import visit as Vi

import Iterator as It
import PathCreator as Pa
import MakeImagesPython as Mk


def Orbit(Files, OrbitOptions, OperatorSet=False):
    """
    Take multiple views around vertically, horizontally, or both.
    Views are evenly spaced.
    OrbitOptions = (<axis>, <number of views>).

    The higher the number of views the smoother the rotation.

    This assumes the following positive axis orientation:
    y - Up
    x - Right
    z - Out from screen
    """

    Pa.PathCreator()  # Creates necessary folders.

    OrbitOptions = tuple(OrbitOptions)

    Line = str(OrbitOptions[0])
    Number = int(OrbitOptions[1])

    Increment = 360.0/float(Number)  # Degrees

    Image = Mk.MakeImages(Files)
    Image.Plot()

    # Multiple Operators.
    try:
        for multiitem in OperatorSet:

            # Apply dictionary operator.
            try:
                Operator = (multiitem.keys())[0]
                List = (multiitem.values())[0]
                Image.Operator(Operator, List, SliceProject=0)
            except Exception:
                pass

            # Apply list operator.
            try:
                Operator = multiitem[0]
                List = multiitem[1]
                Image.Operator(Operator, List, SliceProject=0)
            except Exception:
                pass

    except Exception:
        pass

    # Define which orbits to do.
    orbitSettings = {}
    orbitSettings['vertical'] = {'Line': 0}
    orbitSettings['horizontal'] = {'Line': 1}

    # Choose which orbits to do.
    if OrbitOptions[0].lower() == 'both':
        OrbitOptions = ['vertical', 'horizontal']

    for orbit in OrbitOptions:
        Vi.ResetView()
        try:
            Line = orbitSettings[orbit]["Line"]

            v = Vi.GetView3D()
            v.viewNormal = (0, 0, 1)
            v.viewUp = (0, 1, 0)

            Degrees = 0
            while 360.0 > Degrees:
                # Turning shading False yields black images.
                Image.Save(Shading=True)
                v.RotateAxis(Line, Increment)
                Vi.SetView3D(v)
                Degrees += Increment

        except Exception:
            pass
