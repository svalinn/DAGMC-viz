import xml.etree.ElementTree as ET

tree = ET.parse('Sessions/XML/sample3.session')
root = tree.getroot()

# SOURCE and localhost are the Fields I want to replace
# I have 2*n files to replace with desired files.



# Attains the path for files used
for Field in root.findall("Object/Object/Object/Field"):
	name = Field.get('name')
	if name == 'localhost:/home/lane/Desktop/DAGMC-viz/./Data/meshtal.vtk':
		source1 = name
		print(source1)
	elif name == 'localhost:/home/lane/Desktop/DAGMC-viz/./Data/rmgrave.stl':
		print(name)
		Field.clear()
		Field.tag = ("Field")
		Field.attrib = {
						"name": "localhost:/home/lane/Desktop/DAGMC-viz/./Data/fng_zip.stl",
						"type": "string"
						}
		Field.text = "STL_1.0"
		Field.set('updated','yes')
		print('New path is', name)

tree.write('Sessions/XML/output1.session', encoding="utf-8", xml_declaration=True)