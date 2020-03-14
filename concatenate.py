istring=input().split(',')
length=len(istring)
f_index=istring.index('5')
e_index=istring.index('8')
num1=0
num2=''
for i in range(0,length):
    if(i<f_index or i>e_index):
        num1+=int(istring[i])
        #print('\t',num1)
    else:
        num2+=''.join(istring[i])
        #print('\t',num2)
sum=num1+int(num2)
print(sum)
