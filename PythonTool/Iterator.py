import visit as Vi

# The next line can be commented to import and use in the VisIt GUI.
try:
    Vi.Launch()  # Here to allow import of other modules.
except Exception:
    pass

import PathCreator as Pa
import MakeImagesPython as Mk


def Iterator(Files, OperatorSet=None, SliceProject=1):
    """Iterate through several operator options."""

    Pa.PathCreator()  # Creates necessary folders.
    Image = Mk.MakeImages(Files)
    Image.Plot()

    if OperatorSet is None:
        # If no operators are defined, the image of plots
        # without operators is saved.
        Image.Save()

    else:

        for item in OperatorSet:

            Vi.RemoveAllOperators(all)

            # Apply single dictionary operator.
            try:
                Operator = (item.keys())[0]
                myList = (item.values())[0]
                Image.Operator(Operator, myList, SliceProject)
            except Exception:
                pass

            # Apply single list operator.
            try:
                Operator = item[0]
                myList = item[1]
                Image.Operator(Operator, myList, SliceProject)
            except Exception:
                pass

            # Multiple Operators.
            try:
                for multiitem in item:

                    # Apply dictionary operator.
                    try:
                        Operator = (multiitem.keys())[0]
                        myList = (multiitem.values())[0]
                        Image.Operator(Operator, myList, SliceProject)
                    except Exception:
                        pass

                    # Apply list operator.
                    try:
                        Operator = multiitem[0]
                        myList = multiitem[1]
                        Image.Operator(Operator, myList, SliceProject)
                    except Exception:
                        pass

            except Exception:
                pass

            Image.Save()
