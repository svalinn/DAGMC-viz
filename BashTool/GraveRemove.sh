#!/bin/bash

WithGrave=$1
NoGrave=$2

DATAPATH=../Data
cd "${DATAPATH}"

# Identify graveyard
source ../BashTool/GraveIdentifier.sh

mbconvert $WithGrave -t -v $VolumeIDList -s $SurfaceIDList -c $CurveIDList -V $VertexIDList $NoGrave
