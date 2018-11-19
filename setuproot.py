#!/usr/bin/env python
import re
fname = "setuproot.txt"
myfile = open(fname,"r")
for line in myfile:
	if re.search("recommended",line):
		searchObj = re.search(r'\d\S+',line)
		print searchObj.group()
