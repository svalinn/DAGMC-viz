#!/bin/bash
DATAPATH=../PythonTool/Data
cd "${DATAPATH}"

printf "Include file extensions for naming. \n"

echo -e "File (h5m) for removal of graveyard: "
read WithGrave

# Save the relations.
mbgsets $WithGrave > ../../BashTool/DataFileInfo/Structure.txt

STRUCTUREPATH=../../BashTool/DataFileInfo
cd "${STRUCTUREPATH}"

# Delete everything before line break.
sed '1,/^$/d' Structure.txt > Relations.txt
# Delete everything after line break.
sed '/^$/,$ d' Structure.txt > Geometry.txt

# Get graveyard ID.
GraveID=$(grep graveyard Structure.txt | awk '{print $1;}')

# Get first level ID related to graveyard.
RelationToGraveID=$(grep $GraveID Relations.txt | awk '{print $3;}' | sed 's/;$//')

# Get second level ID related to graveyard.
SecondIDs=$(grep $RelationToGraveID Relations.txt > GraveGeometry.txt)

grep $SecondIDs Geometry.txt > Geology.txt