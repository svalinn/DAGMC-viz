#!/bin/bash
PythonScripts=../PythonTool
cd "${PythonScripts}"

printf "Include file extensions for naming. \n"

echo -e "Name of the original session file: "
read SessionFile

echo -e "Name of original stl file: "
read FileSTLOld

echo -e "Name of original vtk file: "
read FileVTKOld

echo -e "Name of new stl file: "
read FileSTLNew

echo -e "Name of new vtk file: "
read FileVTKNew

python XmlEdit.py $SessionFile $FileSTLOld $FileVTKOld $FileSTLNew $FileVTKNew
