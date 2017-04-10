#!/usr/bin/python
import sys
import datetime
for line in sys.stdin:
	data = line.strip().split("\t")
	if len(data) == 6:
		jour = data[0]
		vente = data[4]
		weekday = datetime.datetime.strptime(jour,"%Y-%m-%d").weekday()
		if weekday == 0:
			print "{0}\t{1}".format("Monday",vente)
		if weekday == 1:
			print "{0}\t{1}".format("Tuesday",vente)
		if weekday == 2:
			print "{0}\t{1}".format("Wednesday",vente)
		if weekday == 3:
			print "{0}\t{1}".format("Thusrday",vente)
		if weekday == 4:
			print "{0}\t{1}".format("Friday",vente)
		if weekday == 5:
			print "{0}\t{1}".format("Saturday",vente)
		if weekday == 6:
			print "{0}\t{1}".format("Sunday",vente)
			
