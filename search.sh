SEARCHTERMS=`echo $@ | sed -e "s/ /+/g"`

wget -O search.html "http://gdata.youtube.com/feeds/api/videos?q=$SEARCHTERMS&max-results=50&prettyprint=true"


grep watch?v= search.html | sed -e "s/.*watch?v=//"|sed -e "s/&amp.*//"|uniq >> searchresults.txt
grep watch?v= search.html | sed -e "s/.*watch?v=//"|sed -e "s/&amp.*//"|uniq >> searchresults.temp
