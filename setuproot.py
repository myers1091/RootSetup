#!/usr/bin/env python
from os.path import expanduser
home = expanduser("~")
import re
TopDir = "/RootSetup/"
fname = "setuproot.txt"
myfile = open(home+TopDir+fname,"r")
for line in myfile:
	if re.search("recommended",line):
		searchObj = re.search(r'\d\S+',line)
		print searchObj.group()
