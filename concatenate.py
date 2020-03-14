'''
Given a list of numbers containing 5 and 8,contruct a num1 by adding all numbers which do not lie between 5 and 8 and num3 by concating the
numbers between 5 and 8(including both) and find the sum of num1 and num2
ex:ip:3,2,6,5,1,4,8,9
   op:5168
'''

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
