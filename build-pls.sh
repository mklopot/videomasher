SEQUENCES=20
LENGTH=16
PERIOD=3
: > back2back-playlist.txt;

for i in `seq 0 $SEQUENCES`;
 do ./back3back-playlist.sh | tail -n$LENGTH >> back2back-playlist.txt; 
 wc back2back-playlist.txt;
done;

mplayer -speed 2 -fs -fixed-vo  -playlist back2back-playlist.txt
