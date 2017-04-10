#!/usr/bin/python
import sys
calcul = 0
for line in sys.stdin:
	data = line.strip().split("\t")	
	if len(data) != 2:
		continue
	calcul = calcul + 1
print "total : ", "\t", calcul

