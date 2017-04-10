#!/usr/bin/python
import sys
for line in sys.stdin:
	data = line.strip().split("\t")
	if data[0] == '"id"' or data[0] == '"user_ptr_id"' or not (data[0][1:len(data[0])-1].isdigit()):
		continue

	if len(data) == 19:
		id = data[0]
		titre = data[1]
		tagname = data[2]
		author_id =  data[3]
		node_type = data[5]
		parent_id = data[6]
		abs_parent_id = data[7]
		added_at = data[8]
		score = data[9]
		line = "2"+"\t"+id+"\t"+titre+"\t"+tagname+"\t"+node_type+"\t"+parent_id+"\t"+abs_parent_id+"\t"+added_at+"\t"+score 
		print "{0}\t{1}".format(author_id,line)
	if len(data) == 5 and data[1][1:len(data[1])-1].isdigit():	
		id = data[0]
		reputation = data[1]
		gold = data[2]
		sliver = data[3]
		bronze = data[4]
		line="1"+"\t"+reputation+"\t"+gold+"\t"+sliver+"\t"+bronze		
		print "{0}\t{1}".format(id,line)
