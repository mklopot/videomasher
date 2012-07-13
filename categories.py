import os

videodir='video/'

directories=os.listdir(videodir)
any=[ os.path.join(videodir,x) for x in directories ]
all=any

for directory in directories:
    commandstring =  '{0} = [os.path.join(videodir,"{0}")]'.format(directory)
    exec(commandstring)
 
#babies = [ os.path.join(videodir,'babies')]

if __name__ == '__main__':
    print any
    print babies
