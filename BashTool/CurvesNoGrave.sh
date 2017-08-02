#!/bin/bash

WithGrave=$1
Curves=$2

DATAPATH=../Data
cd "${DATAPATH}"

# Identify graveyard
source ../BashTool/GraveIdentifier.sh

mbconvert $WithGrave -t -c "$CurveIDList" $Curves
