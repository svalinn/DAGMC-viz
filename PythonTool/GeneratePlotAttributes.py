def GeneratePlotAttributes(File):
    """Generate plot options that the user may define."""

    GeneralSettings = {}

    File = list(File)

    for item in File:
        # Check for optional inputs in Dictionary input.
        try:
            # Change the options for line style.
            Option = "Attribute.lineStyle = Attribute." + str(item[3]).upper()
            GeneralSettings[item[1]] = Option
        except Exception:
            pass

    try:

        return GeneralSettings

    except Exception:
        pass
