#!/usr/bin/env python

import os
import glob

# global variables

packfile = "/home/cjbaccus/Code/python/PyPackInstall/packages2install"

allfiles = open(packfile, "r")

for line in allfiles:
	text = line
	print(text)
	os.system("sudo apt-get install " + line.strip() + " -y\n")

