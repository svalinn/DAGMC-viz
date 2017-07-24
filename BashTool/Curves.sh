#!/bin/bash
WithGrave=$1
FileSTLGrave=$2


DATAPATH=../Data
cd "${DATAPATH}"

# Save the relations.
mbgsets $WithGrave > ../BashTool/DataFileInfo/Structure.txt

STRUCTUREPATH=../BashTool/DataFileInfo
cd "${STRUCTUREPATH}"



# Delete everything after line break.
sed '/^$/,$ d' Structure.txt > Geometry.txt

# Delete everything before line break.
sed '1,/^$/d' Structure.txt > Relations.txt



# Get graveyard ID.
grep graveyard Structure.txt | awk '{print $1;}' > GraveID.txt



# Four levels of filtration should be sufficient for all cases.
# Get first level ID related to graveyard.
while read line
do
	grep -wF "$line" Relations.txt | awk '{print $3;}' | sed 's/;$//'
done < GraveID.txt > Level1.txt

# Get second level ID related to graveyard.
while read line
do
	grep -wF "$line" Relations.txt | awk '{print $3;}' | sed 's/;$//'
done < Level1.txt > Level2.txt

# Get third level ID related to graveyard.
while read line
do
	grep -wF "$line" Relations.txt | awk '{print $3;}' | sed 's/;$//'
done < Level2.txt > Level3.txt

# Get fourth level ID related to graveyard.
while read line
do
	grep -wF "$line" Relations.txt | awk '{print $3;}' | sed 's/;$//'
done < Level3.txt > Level4.txt

# Remove repeating lines.
awk '!seen[$0]++' Level4.txt > GraveRelations.txt


# Graveyard shapes.
while read line
do
	grep -wF "$line" Geometry.txt | awk '{print $4,$5;}' | sed 's/"];$//' | sed 's/^"//'
done < GraveRelations.txt > GraveGeometry.txt

# Non-Graveyard Shapes.
grep -wvf GraveGeometry.txt Geometry.txt > NonGraveGeometry.txt



# Non-Graveyard ID.
grep Volume NonGraveGeometry.txt | awk '{print $5;}' | sed 's/"];$//' > VolumeID.txt
grep Surface NonGraveGeometry.txt | awk '{print $5;}' | sed 's/"];$//' > SurfaceID.txt
grep Curve NonGraveGeometry.txt | awk '{print $5;}' | sed 's/"];$//' > CurveID.txt
grep Vertex NonGraveGeometry.txt | awk '{print $5;}' | sed 's/"];$//' > VertexID.txt



# Convert rows into columns.
sed "s/$/,/g" VolumeID.txt | awk '{printf("%s ",$0)}' > VolumeIDComma.txt
sed "s/$/,/g" SurfaceID.txt | awk '{printf("%s ",$0)}' > SurfaceIDComma.txt
sed "s/$/,/g" CurveID.txt | awk '{printf("%s ",$0)}' > CurveIDComma.txt
sed "s/$/,/g" VertexID.txt | awk '{printf("%s ",$0)}' > VertexIDComma.txt



# Eliminate space between items.
VolumeIDList=$(cat VolumeIDComma.txt | tr -d " \t\n\r")
SurfaceIDList=$(cat SurfaceIDComma.txt | tr -d " \t\n\r")
CurveIDList=$(cat CurveIDComma.txt | tr -d " \t\n\r")
VertexIDList=$(cat VertexIDComma.txt | tr -d " \t\n\r")



DATAPATH=../../Data
cd "${DATAPATH}"



mbconvert $WithGrave -t -c $CurveIDList $FileSTLGrave
