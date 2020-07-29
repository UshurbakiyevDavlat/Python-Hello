fname = input("Enter file name: ")
if len(fname) < 1 : fname = "mbox-short.txt"

fh = open(fname)
count = 0
lst=list()

for line in fh:
	parse=line.split()
	for lin in parse:
    	lst.append(lin)
for line in range(len(lst)):
    if lst[line]=="From":
        print(lst[line+1])
        count+=1




print("There were", count, "lines in the file with From as the first word")
