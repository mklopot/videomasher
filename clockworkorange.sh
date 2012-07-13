#/bin/bash

# EDL toggile is "i"

for file in *{.flv,.mp4,.webm}
do
if [ -f $file.edl ]; then
continue
fi

while true; do
mplayer -fixed-vo -osdlevel 3 -use-filename-title -edlout $file.edl $file

while true
do
echo Finished playing file $file
echo "Accept, Replay, Fail? (a/r/f)"
read -n1 RESPONSE
echo

case $RESPONSE in
f)
rm $file
echo Deleted, real Horrorshow. 
break
;;

a) 
break
;;

r)
mplayer -fixed-vo -osdlevel 3 -use-filename-title -edlout $file.edl $file
continue
;;

*)
echo "Accept, Replay, Fail? (a/r/f)"
;;

esac
done

break

done
done

echo Finished processing files in this folder. 
echo Run edl.sh to process EDL files.
