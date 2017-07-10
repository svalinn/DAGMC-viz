#!/bin/bash
DATAPATH=../PythonTool/Data
cd "${DATAPATH}"

echo -e "File name for h5m to stl conversion: "
read FileH5M
echo -e "Name of stl mesh file: "
read FileSTL

echo -e "File name for cub to vtk conversion: "
read FileCUB
echo -e "Name of vtk file: "
read FileVTK

mbconvert $FileH5M $FileSTL
mbconvert $FileCUB $FileVTK
