#!/usr/bin/python

import shlex
from commands import *

lines=file('commandfile.txt','rt').readlines()
for line in lines:
    tokens=shlex.split(line,1)
    if (len(tokens) > 2):
        function_name=tokens[1]
        exec(function_name+"(tokens)")

