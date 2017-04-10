#!/usr/bin/python
import sys
for line in sys.stdin:
	data = line.strip().split("\t")
	if len(data) == 19:
		body = data[4]
		i = 0
		for lettre in body:
			if lettre == "?" or lettre == "." or lettre == "!":
				i = i + 1
		if  i == 0 or i ==1 or body[len(body)-1] == "." or body[len(body)-1] == "?" or body[len(body)-1] == "!":
			print "{0}\t{1}".format(1,body)
		

