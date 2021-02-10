
import collections
import os
file_to_read = open("access_log1")
read_file = file_to_read.readlines()
list_get_post = []
list_get = []
list_post = []
for i in read_file:
	split_ligne = i.split(" ")
	list_get_post.append(split_ligne)
for y in list_get_post:
	
	if '"GET' in y:
		list_get.append(y)
	if '"POST' in y:
		list_post.append(y)
for z in list_post:
	list_get_data = []
	print(list_get_data[5:7])
