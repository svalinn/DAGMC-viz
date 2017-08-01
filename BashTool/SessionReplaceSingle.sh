#!/bin/bash

# Name of the original session file:
SessionFile=$1

# Name of original stl file:
FileOld=$2

# Name of new stl file:
FileNew=$3

source ../BashTool/SessionReplaceNameIncrement.sh

grep "localhost:" "$SessionFile" | sed "s/$FileOld/$FileNew/g" "$SessionFile" > ../XML_Edited/"$name".session

printf "$name"'.session was saved.\n'
