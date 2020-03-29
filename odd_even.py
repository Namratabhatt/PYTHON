'''
GIVEN A STRING,IF THE NUMBER OF SPECIAL CHARACTERS IN THE GIVEN STRING IS EVEN,
SO WE SHOULD PRINT FIRST EVEN DIGITS AND NEXT ODD DIGITS ALTERNATE IN THE SAME SERIES
AS THEY ARE PRESENT IN THE STRING,AND VICE VERSA FOR ODD
EX:
I/P:A5w8@k7!l23n69
O/P:8527639
'''
even=[]
odd=[]
sp=0
istring=input()

for ch in istring:
    if(ch.isalnum()==False):
        sp+=1
    elif(ch.isdigit()):
        if int(ch)%2==0:
            even.append(ch)
        else:
            odd.append(ch)

if(sp%2!=0):
    odd,even=even,odd
e_len=len(even)
o_len=len(odd)
maxi=max(e_len,o_len)
e=0
o=0
for i in range(maxi):
    if(e!=e_len):
        print(even[e],end='')
        e+=1
    if(o!=o_len):
        print(odd[o],end='')
        o+=1
    