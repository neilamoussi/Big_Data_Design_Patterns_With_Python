#!/usr/bin/python
import sys
oldid = None
idpost = None
titre = None
tagname = None
node_type = None
parent_id = None
abs_parent_id = None
added_at = None
score = None
reputation = None
gold = None
sliver = None
bronze = None
for line in sys.stdin:
	data = line.strip().split("\t")
	thisid = data[0]
	if data[1] == "2":
		idpost = data[2]
		titre = data[3]
		tagname = data[4]
		node_type = data[5]
		parent_id = data[6]
		abs_parent_id = data[7]
		added_at = data[8]
		score = data[9]	
	if data[1] == "1":
        	reputation = data[2]
		gold = data[3]
		sliver = data[4]
		bronze = data[5]
	if idpost and oldid != idpost:
		print "{0}\t{1}\t{2}\t{3}\t{4}\t{5}\t{6}\t{7}\t{8}\t{9}\t{10}\t{11}\t{12}\n".format(idpost,thisid,titre,tagname,node_type,parent_id,abs_parent_id,added_at,score,reputation,gold,sliver,bronze)
	oldid = idpost
"""if oldid != None:
	print "{0}\t{1}\t{2}\t{3}\t{4}\t{5}\t{6}\t{7}\t{8}\t{9}\t{10}\t{11}\t{12}\n".format(idpost,thisid,titre,tagname,node_type,parent_id,abs_parent_id,added_at,score,reputation,gold,sliver,bronze)"""
