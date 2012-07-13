from playlist import *

playlist=[]
while ( len(playlist) < 880 ):
    playlist = playlist + picklist(['chunks-3'])
    playlist = playlist + picklist(['chunks-3'])
    playlist = playlist + picklist(['rawstatic'])
    playlist = playlist + picklist(['rawstatic'])
    playlist = playlist + picklist(['chunks-4'])
    playlist = playlist + picklist(['chunks-4'])
    playlist = playlist + picklist(['rawstatic'])
    playlist = playlist + picklist(['rawstatic'])

for item in playlist:
    print item

