#!/bin/bash

for file in *flv.*.mp4
do
number=`echo $file|cut -f3 -d.`
name=`echo $file|cut -f1 -d.`
echo $name
echo $number
mv $file $name.flv.`printf %05d $number`.mp4
done

for file in *mp4.*.mp4
do
number=`echo $file|cut -f3 -d.`
name=`echo $file|cut -f1 -d.`
echo $name
echo $number
mv $file $name.mp4.`printf %05d $number`.mp4
done

