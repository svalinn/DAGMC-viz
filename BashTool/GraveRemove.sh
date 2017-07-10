#!/bin/bash
DATAPATH=../PythonTool/Data
cd "${DATAPATH}"

echo -e "File for removal of graveyard: "
read WithGrave

mbgsets $WithGrave > ../../BashTool/DataFileInfo/Structure.txt

STRUCTUREPATH=../../BashTool/DataFileInfo
cd "${STRUCTUREPATH}"
pwd

grep s3376 Structure.txt