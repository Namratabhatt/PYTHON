n=[10,9,4,5,7,2,8,20,21]
m=15

rems={}
for i in n:
    remind=i%m
    if remind in rems:
        rems[remind]+=1
    else:
        rems[remind]=1
#print(rems)
pairs=0
for r in rems:
    complement=m-r
    if(complement==0 or 2*complement==m):
        pairs+=(rems[r]*(rems[r]-1))//2
    elif(complement) in rems:
        pairs+=rems[r]*rems[complement]
        rems[r]=0
    #print(r,pairs)

print(pairs)