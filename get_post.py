
from collections import Counter 
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
		list_get.append(y[6])

	if '"POST' in y:
		list_post.append(y[6])
list_get_data = Counter(list_get)
list_post_data = Counter(list_post)
print ("choix du type POST ou GET \n")
choix_input= input("GET or POST \n")
if choix_input == "GET":
	print(*list_get_data, sep="\n")
else:
	print("\n" .join(list_post_data))

