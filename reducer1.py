#!/usr/bin/python
import sys
nbre = 0
oldword = None
liste = []
for line in sys.stdin:
	data = line.strip().split("\t")
	if len(data) != 2:
		continue
	thisword, thisid= data
	if oldword and oldword != thisword:
		print "{0}\t{1}\t{2}".format(oldword,nbre,liste)
		nbre = 0
		liste=[]
	oldword = thisword
	nbre += 1
	liste.append(thisid)
if oldword != None:
	print "{0}\t{1}\t{2}".format(oldword,nbre,liste)

