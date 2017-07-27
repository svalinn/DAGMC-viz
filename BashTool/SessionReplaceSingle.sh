#!/bin/bash
SESSIONS=../Sessions/XML_Original/
cd "${SESSIONS}"



#Name of the original session file:
SessionFile=$1

# Name of original stl file:
FileSTLOld=$2

# Name of new stl file:
FileSTLNew=$3



name=../XML_Edited/edited
if [[ -e $name"0.session" ]] ; then
    i=0
    while [[ -e $name$i.session ]] ; do
        let i++
    done
    name=$name$i
else
	name=../XML_Edited/edited0
fi



grep "localhost:" "$filename" | sed "s/$FileSTLOld/$FileSTLNew/g" $SessionFile > ../XML_Edited/"$name".session

printf "$name"'.session was saved.\n'
