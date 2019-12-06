#!/usr/bin/env python

import os
import glob

# global variables

pipfile = "/home/cjbaccus/Code/python/PyPackinstall/Pippacks"

allfiles = open(pipfile, "r")

for line in allfiles:
	text = line
	print(text)
	os.system("sudo pip install " + line)

