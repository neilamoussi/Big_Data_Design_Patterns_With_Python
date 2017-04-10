#!/usr/bin/python
import sys
somme = 0
oldday = None
for line in sys.stdin:
	data = line.strip().split("\t")
	if len(data) != 2:
		continue
	thisday, thisvente= data
	if oldday and oldday != thisday:
		print "{0}\t{1}".format(oldday,somme)
		somme = 0
	oldday = thisday
	somme = somme + float (thisvente)
if oldday != None:
	print "{0}\t{1}".format(oldday,somme)
