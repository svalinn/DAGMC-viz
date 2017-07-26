import os

import visit as Vi
Vi.Launch()


def GrabImagesFromOtherSources(Data):
	"""Reload sessions with different sources"""

	DataSource = []
	for item in Data:
		DataSource.append("../Data/"+item)

	DataSource = tuple(DataSource)

	Directory = str(os.getcwd())+"/../Sessions/XML_Original"

	for file in sorted(os.listdir(Directory)):
		if file.endswith(".session"):
			Vi.RestoreSessionWithDifferentSources(
												  os.path.join(Directory, file),
												  0,
												  DataSource,
												  )
			Vi.RecenterView()
			Vi.SaveWindow()  # Save directory defined by session.
