import collections 
file_log = open("access_log")
lines = file_log.readlines()
list = []
listpub = []
listpriv = []
for line in lines:
	line_split = line.split(" ")
	list.append(line_split[0])
for results in list:
	if "192.168." in results:
		listpub.append(results)
		
	else:
		listpriv.append(results)
count_listpriv = collections.Counter(listpriv)
count_listpub = collections.Counter(listpub)
print ( " " )
print("\033[2;31;31m Address Privé\033[0;37;00m \n")
print(count_listpriv)
print ( " ")
print("\033[2;31;31m Address Publique\033[0;37;00m \n")
print(count_listpub)
print ("choissir une ip a analyser")
choix = input()
for i in lines:
	if choix in i:
		print (i)
