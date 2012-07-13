#/bin/bash

shopt -s extglob

for edlfile in `ls *.edl`
do filename=${edlfile%.edl}
echo $edlfile
echo $filename
mencoder -edl $edlfile  -ovc copy -nosound -o $filename.edl.flv $filename!(*edl)
rm $filename!(*edl.flv)
done



