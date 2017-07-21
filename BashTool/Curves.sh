#!/bin/bash
DATAPATH=../Data
cd "${DATAPATH}"



# File (h5m) for removal of graveyard:
Original=$1

# Name of no grave yard stl mesh file:
CurvesOnly=$2



mbconvert -1 $Original curves.h5m
mbconvert curves.h5m $CurvesOnly

rm curves.h5m