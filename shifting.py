istring=input().split(',')
for i in istring:
    temp=i.split(':')
    name=temp[0]
    length=len(name)
    numb=temp[1]
    sq=0
    for i in numb:
        sq+=int(i)**2

    if(sq%2==0):
        s=name[length-2:]
        print(s+name[:length-2],end=' ')
    else:
        s=name[0]
        print(name[1:]+s,end=' ')

