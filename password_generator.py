istring=input().split(',')
finals=''
for i in istring:
    temp=i.split(':')
    name=temp[0]
    numb=temp[1]

    max=0
    for dig in numb:
        if(int(dig)<len(name)):
            if(int(dig)>max):
                max=int(dig)
    if(max==0):
        finals+='X'
    else:
        finals+=name[max-1]
print(finals)
