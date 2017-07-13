#!/bin/bash
SESSIONS=../Sessions/XML_Original/
cd "${SESSIONS}"

printf "Include file extensions. \n"



echo -e "Name of the original session file: "
read SessionFile

echo -e "Name of original stl file: "
read FileSTLOld

echo -e "Name of new stl file: "
read FileSTLNew



name=../XML_Edited/edited
if [[ -e $name.session ]] ; then
    i=0
    while [[ -e $name$i.session ]] ; do
        let i++
    done
    name=$name$i
fi



sed "s/$FileSTLOld/$FileSTLNew/g" $SessionFile > ../XML_Edited/"$name".session

printf "$name"'.session was saved.'
