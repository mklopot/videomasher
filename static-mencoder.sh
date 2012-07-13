for w in 8 16 32 64 128 256 640
do
  for h in 4 9 18 36 72 144 480
  do

    for fps in 3 6 12 23 30 
    do

      for unsharp in 1 3 5 17
      do

       for vf in "" ",tfields" ",tfields,tfields"
       do
         #mencoder -demuxer rawvideo -rawvideo w=64:h=32:fps=24:format=yuy2 -ovc lavc -vf scale=640:480,unsharp=l3x3:-30,hue=0:10 -ss 120 -endpos 60 /dev/urandom -o downloads/randomraw64x32.mp4 
echo $w $h $fps $unsharp $vf
         mencoder -demuxer rawvideo -rawvideo w=$w:h=$h:fps=$fps:format=yuy2 -ovc lavc -vf scale=640:480,unsharp=l$unsharpx$unsharp:-30,hue=0:10$vf -ss 120 -endpos 60 /dev/urandom -o rawstatic-$w-$h-$fps-$unsharp-$vf.avi 
        done 
       done
     done
   done
done
