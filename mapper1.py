#!/usr/bin/python
import sys
for line in sys.stdin:
	data = line.strip().split("\t")
	if len(data) == 19:
		id = data[0]
		body = data[4]
		ch = ""
		for lettre in body:
			if lettre != "." and lettre != "?" and lettre != "!" and lettre != ":" and lettre != ";" and lettre != '"' and lettre != "(" and lettre != ")" and lettre != "<" and lettre != ">" and lettre != "#" and lettre != "$" and lettre != "=" and lettre != "-" and lettre != "/" and lettre != " ":
				ch = ch + lettre
			else:
				if len(ch) != 0:
					print "{0}\t{1}".format(ch,id)
					ch=""
			
