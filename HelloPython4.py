fname = input("Enter file name: ")
fh = open(fname)
lst = list()

for line in fh:
	s=line.split()
	for l in s:
    	if l not in lst:
       		lst.append(l)
        

lst.sort()

print(lst)
