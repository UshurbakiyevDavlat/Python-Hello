import re
fname=input("File name:")
handle=open(fname)

total=list()

for numbers in handle:
    numbers=numbers.rstrip()
    parse=numbers.split()
    for ctr in parse:
        count=re.findall('[0-9]+',ctr)
        if len(count)!=1:continue
        num=float(count[0])
        total.append(num)

print("Total is:",sum(total))
print(total)
