import xml.etree.ElementTree as ET
import argparse
import os

import Inputs

parser = argparse.ArgumentParser(description='Change names of files in session.',
                                usage='Insert the old session file and write a new session file.',
                                )

parser.add_argument("-cr", "--Create",
                    help="add plots of data",
                    action="store_true",
                    )
parser.add_argument("Original",
					help="The path of the original session file."
					)
parser.add_argument("New",
					help="The path of the wanted session file."
					)

args = parser.parse_args()

def XmlEdit(Original, New):

	tree = ET.parse(Original)
	root = tree.getroot()

	# SOURCE* and localhost* are the Fields I want to replace under the ViewerSubject object.

	# Attains the path for files used.
	for Field in root.findall("Object/Object/Object/Field"):
		name = Field.get('name')
		if name == "localhost:"+str(os.getcwd())+"/./Data/dummy.stl":
			print(name)
			Field.clear()
			Field.tag = ("Field")
			Field.attrib = {
							"name": "localhost:"+str(os.getcwd())+New,
							"type": "string"
							}
			Field.text = "STL_1.0"

	tree.write('Sessions/XML/output3.session', encoding="utf-8", xml_declaration=True) # Should be incrementable



#Original = 'Sessions/XML/sample5.session'
#New = "/./Data/fng_zip.stl"

if args.Create:
	Original = args.Original
	New = args.New
	XmlEdit(Original, New)
