#!/bin/bash

WithGrave=$1
Surfaces=$2

DATAPATH=../Data
cd "${DATAPATH}"

# Identify graveyard
source ../BashTool/GraveIdentifier.sh

mbconvert $WithGrave -t -s $SurfaceIDList $Surfaces
