import playlist
from categories import *

def intercut(commandline):
    dirs=",".join(commandline[3:])
    iter=int(commandline[0])
    cuts=int(commandline[2])
    playlist.intercut(eval(dirs),cuts,iter)

def cycle(commandline):
    dirs=",".join(commandline[3:])
    iter=int(commandline[0])

    if commandline[2].isdigit():
        cuts=int(commandline[2])
    else:
        cuts=1

    playlist.sequence(list(eval(dirs)),cuts,iter)


def random(commandline):
    iter=int(commandline[0])
    odds=[eval(x.replace(":",",")) for x in commandline[2:]]
    playlist.pickodds(odds,iter)

