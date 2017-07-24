#!/bin/bash
SESSIONS=../Sessions/XML_Original/
cd "${SESSIONS}"



# Name of original stl file:
FileSTLOld=$1

# Name of new stl file:
FileSTLNew=$2





for filename in *.session

do
	name=../XML_Edited/edited
	if [[ -e $name.session ]] ; then
	    i=0
	    while [[ -e $name$i.session ]] ; do
	        let i++
	    done
	    name=$name$i
	fi

	sed "s/$FileSTLOld/$FileSTLNew/g" "$filename" > ../XML_Edited/"$name".session

done




printf "Session files where changed.\n"
