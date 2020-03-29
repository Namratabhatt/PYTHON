'''
GIVEN A STRING THE TASK IS TO PERFORM GROUP OF SIMILAR ALPHABETS
INTHE ORDER THEY APPEAR IN INPUT STRING THEN ARRANGE THEM IN ALPHBETICAL ORDER
THEN PRINT 1ST GROUP FROM ASCENDING FOLLOWED BY LAST GROUP IN ASCENDING
EX:I/P:HeLloOWorLDd
   O/P:DdWerHoOoLlL
'''

istring=list("HeLloOWorLDd")
leng=len(istring)
char_list=[]

for i in range(leng):
    if(istring[i]==''):
        continue
    char_grp=istring[i]
    for j in range(i+1,leng):
        if(istring[i].lower()==istring[j].lower()):
            char_grp+=istring[j]
            istring[j]=''
    istring[i]=''
    char_list.append(char_grp)

for i in range(len(char_list)):
    for j in range(i+1,len(char_list)):
        if(char_list[i].lower()>char_list[j].lower()):
            temp=char_list[i]
            char_list[i]=char_list[j]
            char_list[j]=temp

length=len(char_list)
for i in range(length//2):
    print(char_list[i]+char_list[length-i-1],end='')
if(length%2!=0):
    print(char_list[length//2])

