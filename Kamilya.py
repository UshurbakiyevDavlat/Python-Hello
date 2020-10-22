n=int(input("Enter n \n"))
arr=[]
ctr=0
ctr1=0

for i in range(int(n)):
    arr.append(input(""))

for i in arr:
    if(ctr1<ctr):
        ctr1=ctr
    ctr=0
    for j in arr:
        if(i==j):
            ctr+=1
res=n-ctr1
print("Answer is:" + str(res))
