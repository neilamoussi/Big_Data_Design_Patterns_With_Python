#!/usr/bin/python
import sys
nbr = 0
moyenne = 0
somme = 0
oldday = None
for line in sys.stdin:
	data = line.strip().split("\t")
	if len(data) != 2:
		continue
	thisday, thisvente= data
	if oldday and oldday != thisday:
		moyenne = somme / nbr
		print "{0}\t{1}".format(oldday,moyenne)
		somme = 0
		nbr = 0
	oldday = thisday
	nbr = nbr + 1
	somme = somme + float (thisvente)
if oldday != None:
	moyenne = somme / nbr
	print "{0}\t{1}".format(oldday,moyenne)
