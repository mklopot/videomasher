#!/bin/bash

YOUTUBEDL=/home/f/videomasher/youtube-dl

cd downloads
mkdir $1
cd $1

for video in `cat ../../searchresults.txt`; 
  #do sed 1d ../searchresults.txt > ../searchresults.temp
  do grep -v $video ../../searchresults.txt > ../../searchresults.temp
  #../youtube-dl -c -t -- "$video"; 
  timeout 300 $YOUTUBEDL -c -t -- "$video"; 

  if [ $? == 0 ]
    then
    cp ../../searchresults.temp ../../searchresults.txt
  fi
done
