# Use the file name mbox-short.txt as the file name
fname = input("Enter file name: ")
fh = open(fname)

count=0
av=0

for line in fh:

    if not line.startswith("X-DSPAM-Confidence:") : continue
    else:
        count+=1
        ind=line.find('0')


    av+=float(line[ind:ind+6])

print("Average spam confidence:",av/count)
