name = input("Enter file:")
if len(name) < 1 : name = "mbox-short.txt"
handle = open(name)

d=dict()
count=0

for names in handle:
	if names.startswith("From "):
    	names=names.split()

    	for name in names:

    		d[name]=d.get(name,0)+1



coun_big=None
coun_name=None

for name,count in d.items():
  	if "@" in name:
		if coun_big==None or count>coun_big:
    		coun_name=name
    		coun_big=count

print(coun_name,coun_big)
