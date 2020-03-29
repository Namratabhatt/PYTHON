'''
GIVEN A SET OF NUMBER AND THE SUM,WE HAVE TO PRINT THE NO OF COMBINATIONS
POSSIBLE OF LENGTH 4 WHICH SUM IS EQUAL TO GIVEN SUM
I/P:-1,1,0,0,2,-2
O/P:(-1,1,2,-2)(0,0,1,-1)(0,0,-2,2)
'''

import itertools
istring=list(map(int,input().split(",")))
s=0
combi=list(itertools.combinations(istring,4))
#print(combi)
count=0
for i in combi:
    summ=sum(i)
    if(summ==s):
        count+=1
        #print(combi)
print(count)