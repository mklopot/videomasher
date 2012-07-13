#   _      __           ____         _______       _     __                 ______
#  | | /| / /__ _____  / __ \___    / ___/ /  ____(_)__ / /___ _  ___ ____ / / / /
#  | |/ |/ / _ `/ __/ / /_/ / _ \  / /__/ _ \/ __/ (_-</ __/  ' \/ _ `(_-</_/_/_/ 
#  |__/|__/\_,_/_/    \____/_//_/  \___/_//_/_/ /_/___/\__/_/_/_/\_,_/___(_|_|_)  
############################################################                                                
from categories import * 
from playlist import *
############################################################
for i in range(4):
    intercut([static,static,static],5)
for i in range(42):
    intercut([woofers,santa,static],5)
for i in range(12):
    intercut([reindeer,santa],5)
randseq(reindeer,100)
randseq(presents,30)
randseq(timelapse,20)

for i in range(12):
    intercut([amanita,santa],5)
for i in range(12):
    intercut([presents,woofers],5)

for i in range(20):
    pickodds([(family,1),(presents,10)])
for i in range(10):
    pickodds([(presents,5),(woofers,1),(santa,1)])
for i in range(12):
    intercut([santa,presents],4)
 
randseq(santa,20)

randseq(all,50)

for i in range(12):
    intercut([santa,presents,woofers],4)

for i in range(12):
    intercut([presents,presents],5)
for i in range(12):
    intercut([cooking,presents],5)
for i in range(12):
    intercut([santa,amanita],5)
for i in range(12):
    intercut([presents,mushroom],5)
for i in range(12):
    intercut([christmas+hanukkah,woofers],5)

randseq(cooking,20)

randseq(static, 30)
