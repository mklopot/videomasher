#!/bin/bash

CHUNKSIZE=3
CHUNKMAXSTART=30
OFFSET=10

shopt -s extglob

cd downloads2/

#for file in *
for file in !(*.part)
#do SEEK=0
do SEEK=$OFFSET

  if [ -f "../chunks/$file.0.mp4" ] 
    then
    echo "Chunk(s) of $file already exist(s), skipping..."
    continue 
  fi

  while [ $SEEK -lt $CHUNKMAXSTART ]
    #do ffmpeg -an -i $file -ss $SEEK -t $CHUNKSIZE ../chunks/$file.$SEEK.mp4
    do mencoder -nosound -ovc lavc -vf scale=640:480 -ofps 30 -ss $SEEK -endpos $CHUNKSIZE $file -o ../chunks/$file.`printf "%05d" $SEEK`.mp4
    filesize=`stat --printf=%s ../chunks/$file.$(printf "%05d" $SEEK).mp4`
    echo $filesize

    SEEK=`expr $SEEK + $CHUNKSIZE`;

      if [ "$filesize" -lt "1024" ]; then break; 
      fi;


  done;
done;
