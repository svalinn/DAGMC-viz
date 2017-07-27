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
	if [[ -e $name"0.session" ]] ; then
	    i=0
	    while [[ -e $name$i.session ]] ; do
	        let i++
	    done
	    name=$name$i
	else
		name=../XML_Edited/edited0
	fi

	grep "localhost:" "$filename" | sed "s/$FileSTLOld/$FileSTLNew/g" "$filename" > ../XML_Edited/"$name".session

done




printf "Session files where changed.\n"
