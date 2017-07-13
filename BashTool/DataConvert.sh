#!/bin/bash
DATAPATH=../Data
cd "${DATAPATH}"

printf "Include file extensions for naming. \n"



read -r -p "Convert h5m to stl? (yes/no): " response1
if [[ "$response1" =~ ^([yY][eE][sS]|[yY])+$ ]]
then
    echo -e "File name for h5m to stl conversion: "
	read FileH5M

	echo -e "Name of stl mesh file: "
	read FileSTL
fi



read -r -p "Convert cub to vtk? (yes/no): " response2
if [[ "$response2" =~ ^([yY][eE][sS]|[yY])+$ ]]
then

	echo -e "File name for cub to vtk conversion: "
	read FileCUB

	echo -e "Name of vtk file: "
	read FileVTK

fi




if [[ "$response1" =~ ^([yY][eE][sS]|[yY])+$ ]]
then
	mbconvert $FileH5M $FileSTL
fi



if [[ "$response2" =~ ^([yY][eE][sS]|[yY])+$ ]]
then
	mbconvert $FileCUB $FileVTK
fi
