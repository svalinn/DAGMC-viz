import xml.etree.ElementTree as ET
import argparse
import os


parser = argparse.ArgumentParser(description="Replaces files in session.",
                                 usage="Old session file to new session file.",
                                 )

parser.add_argument("-cr", "--Create",
                    help="add plots of data",
                    action="store_true",
                    )
parser.add_argument("Original",
                    help="The path of the original session file.",
                    )
parser.add_argument("NewSTL",
                    help="The path of the wanted session file (stl portion).",
                    )
parser.add_argument("NewVTK",
                    help="The path of the wanted session file (vtk portion).",
                    )

args = parser.parse_args()


def XmlEdit(Original, NewSTL, NewVTK):

    tree = ET.parse(Original)
    root = tree.getroot()

    # SOURCE* and localhost* are the Fields under the ViewerSubject object
    # that are replaced.

    # Attains the path for files used.
    for Field in root.findall("Object/Object/Object/Field"):
        name = Field.get('name')
        nametext = Field.text

        # STL portion
        if name == "localhost:"+str(os.getcwd())+"/./Data/dummy.stl":
            Field.clear()
            Field.tag = ("Field")
            Field.attrib = {
                            "name": "localhost:"+str(os.getcwd())+NewSTL,
                            "type": "string"
                            }
            Field.text = "STL_1.0"
        if nametext == "localhost:"+str(os.getcwd())+"/./Data/dummy.stl":
            Field.text = "localhost:"+str(os.getcwd())+NewSTL

        # VTK portion
        if name == "localhost:"+str(os.getcwd())+"/./Data/dummy.vtk":
            Field.clear()
            Field.tag = ("Field")
            Field.attrib = {
                            "name": "localhost:"+str(os.getcwd())+NewVTK,
                            "type": "string"
                            }
            Field.text = "VTK_1.0"
        if nametext == "localhost:"+str(os.getcwd())+"/./Data/dummy.vtk":
            Field.text = "localhost:"+str(os.getcwd())+NewVTK

    i = 0
    while os.path.exists("Sessions/XML/Edited/output%s.session" % i):
        i += 1

    tree.write("Sessions/XML/Edited/output%s.session" % i,
               encoding="utf-8",
               xml_declaration=True,
               )

if args.Create:
    Original = "Sessions/XML/Original/"+str(args.Original)
    NewSTL = "/./Data/"+str(args.NewSTL)
    NewVTK = "/./Data/"+str(args.NewVTK)
    XmlEdit(Original, NewSTL, NewVTK)
