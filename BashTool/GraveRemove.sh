#!/bin/bash
DATAPATH=../PythonTool/Data
cd "${DATAPATH}"

printf "Include file extensions for naming. \n"

echo -e "File (h5m) for removal of graveyard: "
read WithGrave

mbgsets $WithGrave > ../../BashTool/DataFileInfo/Structure.txt

STRUCTUREPATH=../../BashTool/DataFileInfo
cd "${STRUCTUREPATH}"

sed '1,/^$/d' Structure.txt > Relations.txt
sed '/^$/,$ d' Structure.txt > Geometry.txt

GraveID=$(grep graveyard Structure.txt | awk '{print $1;}')

RelationToGraveID=$(grep $GraveID Relations.txt | awk '{print $3;}' | sed 's/;$//')

grep $RelationToGraveID Relations.txt > GraveGeometry.txt