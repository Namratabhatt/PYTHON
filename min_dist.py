'''GIVEN THE NUMBER OF ELEMENTS TO BE DELETED AND
A LIST(COMBINATION OF REPEATED AND DISTINCT ELEMENTS)
YOU HAVE TO DELETE ANY ELEMENT FROM THE LIST SUCH THAT
YOU WILL HAVE MINIMUN DISTINCT NUMBER OF ELEMENTS

EX:I/P:3
       1 1 1 2 2 2 4 5 6
   O/P:2
'''

rem=int(input())
istring=list(map(int,input().split(" ")))

dist=set(istring)
dist_list=[]

for i in dist:
    count=istring.count(i)
    dist_list.append(count)

dist_list.sort()
leng=len(dist_list)

for i in dist_list:
    if(i<rem):
        rem-i
        leng-=1
    else:
        break

print(leng)

