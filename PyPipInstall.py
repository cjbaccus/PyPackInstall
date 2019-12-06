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

print("\n\nAll done with python 2 pip installs\n\n")
print("*"*50)

for line3 in allfiles:
	text = line
	print("installing PIP3 package")
	print("~"*50)
	os.system("sudo python3 -m pip install " + line)

print("\n\nAll Python3 PIP packages complete\n\n")
print("~"*50)

