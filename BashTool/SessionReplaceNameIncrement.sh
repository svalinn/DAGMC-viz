#!/bin/bash

SESSIONS=../Sessions/XML_Original/
cd "${SESSIONS}"

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

echo "$name"