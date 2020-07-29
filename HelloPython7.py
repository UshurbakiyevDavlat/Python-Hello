name = input("Enter file:")
if len(name) < 1 : name = "mbox-short.txt"
handle = open(name)

d=dict()
for data in handle:
    if data.startswith("From "):
        data=data.split()

	for s in data:
    	d[s]=d.get(s,0)+1

lst=list()

for key,val in d.items():
    newtup=(val,key)
    lst.append(newtup)

lst=sorted(lst,reverse=True)



v=dict()

for val,key in lst[:]:
	val=0
	if ":" in key:
		v[key[:2]]=v.get(key[:2],val)+1


for count,val in sorted(v.items()):
    print(count,val)
