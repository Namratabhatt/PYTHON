'''GIVEN AN ARRAY WITH ELEMENTS SEPARATED USING COMMA(,)
YOU HAVE TO FIND THE LARGEST FIBONACCI SERIES POSSIBLE
OUT OF THE GIVEN ELEMENTS IN THE ARRAY AND PRINT IT
EX:I/P:2,6,3,5,8,9
   O/P:2,3,5,8
'''

istring=list(map(int,input().split(",")))
leng=len(istring)
new_string=[]

for i in range(0,leng):
    for x in range(i+1,leng):
        first=istring[i]
        second=istring[x]
        fab_list=[]
        fab_list.append(first)
        fab_list.append(second)
        for y in range(x+1,leng):
            if(first+second==istring[y]):
                fab_list.append(istring[y])
                first=second
                second=istring[y]
        if(len(new_string)<len(fab_list)):
            new_string=fab_list

if(len(new_string)>2):
    print(new_string)
else:
    print("0")