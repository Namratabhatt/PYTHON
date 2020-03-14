istring=input()
lenght=len(istring)
l=[]
for i in istring:
    if i not in l:
        if(i.isdigit()):
            l.append(i)

l.sort()
l.reverse()
#print(l)
number=int(''.join(l))

if(number%2==0):
    print(number)
else:
    leng=len(l)
    for i in range(leng-1,0,-1):
        if(int(l[i])%2==0):
            d=l[i]
            l.remove(d)
            #l.insert(leng-1,digit)
            l.append(d)
            #print(l)
            e_num=int(''.join(l))
            print(e_num)
            break
    else:
        print(-1)

