import random
import os
import sys

def relpath(directory):
    ls=os.listdir(directory)
    lsrel=[ os.path.join(directory,x) for x in ls ]
    return lsrel

def randlist(directories,n=1):
    rlist=[]
    for directory in directories:
        rlist=rlist+relpath(directory)
    return random.sample(rlist,n)

def sequencelist(dirsrun,length=8):
    dirs=list(dirsrun)
    filelist=[]

    for entry in dirs:
        runlist=[]

        while len(runlist) <= length: 
            pick=randlist(entry).pop()
            runlist=filter(lambda x: x[0:-16] == pick[0:-16], relpath(os.path.dirname(pick)))

        runlist.sort()
        choice=len(runlist)-length

        if (choice == 1):
            start=1
        else:
            start=random.randrange(1,len(runlist)-length)

        runlist=runlist[start:start+length]
        filelist.append(runlist)

    return filelist

def intercutlist(dirs,length=8):
        l=sequencelist(dirs,length)
        return zip(*l)

def randseq(directories,n=1): 
    for item in randlist(directories,n):
        print item

def pickoddslist(odds,iter=1):
    plist=[]
    while len(plist) < iter:
        for oddsentry in odds:
            if len(oddsentry) < 2:
                oddsentry=(oddsentry,1)
            directories,fraction=oddsentry 
            plist=plist+randlist(directories,fraction)
    return random.sample(plist,iter)

def pickodds(odds,iter=1):
   plist=pickoddslist(odds,iter)
   for item in plist:
       print item

def sequence(dirs,length=8,iter=1):
    seqlist=[]
    for i in range(iter):
        seqlist=seqlist+sequencelist(dirs,length)
    for selist in seqlist:
        for item in selist:
            print  item

def intercut(dirs,length=8,iter=1):
    ilist=[]
    for i in range(iter):
        ilist = ilist + intercutlist(dirs,length)
    for tuple in ilist:
        for item in tuple:
            print item

        
if __name__ == '__main__':

    print "randseq():"
    randseq(['video/swimsuit','video/octopus'], n=5)
    print "pickodds():"
    pickodds([(['video/baddancing'],2), (['video/gameshow'],1)],6)
    print "sequence():"
    sequence([['video/monstertruck', 'video/babies'],['video/godzilla','video/octopus']],2,2)
    print "intercut():"
    intercut([['video/babies', 'video/baddancing', 'video/monsters'],['video/static']],5,3)
