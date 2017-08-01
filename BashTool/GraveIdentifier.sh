#!/bin/bash

WithGrave=$1

DATAPATH=../Data
cd "${DATAPATH}"

# Save the relations.
Structure="$(mbgsets $WithGrave)"

# Delete everything after line break.
Geometry=$(echo "$Structure" | sed '/^$/,$ d')
# Delete everything before line break.
Relations=$(echo "$Structure" | sed '1,/^$/d')

# Get graveyard ID.
GraveID=$(echo "$Structure" | grep graveyard | awk '{print $1;}')

# Four levels of filtration should be sufficient for all cases.
# Get first level ID related to graveyard.
Level1=$(echo "$Relations" | grep -we "$GraveID" | awk '{print $3;}' | sed 's/;$//')
# Get second level ID related to graveyard.
Level2=$(echo "$Relations" | grep -we "$Level1" | awk '{print $3;}' | sed 's/;$//')
# Get third level ID related to graveyard.
Level3=$(echo "$Relations" | grep -we "$Level2" | awk '{print $3;}' | sed 's/;$//')
# Get fourth level ID related to graveyard.
Level4=$(echo "$Relations" | grep -we "$Level3" | awk '{print $3;}' | sed 's/;$//')

# Remove repeating lines.
GraveRelations=$(echo "$Level4" | awk '!seen[$0]++')

# Graveyard shapes.
GraveGeometry=$(echo "$Geometry" | grep -we "$GraveRelations" | awk '{print $4,$5;}' | sed 's/"];$//' | sed 's/^"//')
# Non-Graveyard Shapes.
NonGraveGeometry=$(echo "$Geometry" | grep -wve "$GraveGeometry")

# Non-Graveyard ID.
VolumeID=$(echo "$NonGraveGeometry" | grep Volume | awk '{print $5;}' | sed 's/"];$//')
SurfaceID=$(echo "$NonGraveGeometry" | grep Surface | awk '{print $5;}' | sed 's/"];$//')
CurveID=$(echo "$NonGraveGeometry" | grep Curve | awk '{print $5;}' | sed 's/"];$//')
VertexID=$(echo "$NonGraveGeometry" | grep Vertex | awk '{print $5;}' | sed 's/"];$//')

# Convert rows into columns.
VolumeIDComma=$(echo "$VolumeID" | sed "s/$/,/g" | awk '{printf("%s ",$0)}')
SurfaceIDComma=$(echo "$SurfaceID" | sed "s/$/,/g" | awk '{printf("%s ",$0)}')
CurveIDComma=$(echo "$CurveID" | sed "s/$/,/g" | awk '{printf("%s ",$0)}')
VertexIDComma=$(echo "$VertexID" | sed "s/$/,/g" | awk '{printf("%s ",$0)}')

# Eliminate space between items.
VolumeIDList=$(echo "$VolumeIDComma" | tr -d " \t\n\r")
SurfaceIDList=$(echo "$SurfaceIDComma" | tr -d " \t\n\r")
CurveIDList=$(echo "$CurveIDComma" | tr -d " \t\n\r")
VertexIDList=$(echo "$VertexIDComma" | tr -d " \t\n\r")

echo "$VolumeIDList"
echo "$SurfaceIDList"
echo "$CurveIDList"
echo "$VertexIDList"
