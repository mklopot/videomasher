#!/usr/bin/python

import os
import random
where = 'chunks' # source directory

ls = os.listdir(where)
#print ls
print random.choice(ls)

