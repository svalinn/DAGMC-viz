#!/bin/bash

read -r -p "Remove graveyard? (yes/no): " response
if [[ "$response" =~ ^([yY][eE][sS]|[yY])+$ ]]
then
    bash GraveRemove.sh
fi

read -r -p "Convert h5m to stl and/or cub to vtk? (yes/no): " response
if [[ "$response" =~ ^([yY][eE][sS]|[yY])+$ ]]
then
    bash DataConvert.sh    
fi

read -r -p "Create images with VisIt? (yes/no): " response
if [[ "$response" =~ ^([yY][eE][sS]|[yY])+$ ]]
then
    bash VisItOptions.sh
fi

read -r -p "Replace stl data from session file? (yes/no): " response
if [[ "$response" =~ ^([yY][eE][sS]|[yY])+$ ]]
then
    bash SessionReplace.sh
fi