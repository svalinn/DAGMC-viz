#!/bin/bash
DATAPATH=../Data
cd "${DATAPATH}"



# File (h5m) for removal of graveyard:
Original=$1

# Name of no grave yard stl mesh file:
SurfacesOnly=$2



mbconvert -2 $Original surfaces.h5m
mbconvert surfaces.h5m $SurfacesOnly

rm surfaces.h5m