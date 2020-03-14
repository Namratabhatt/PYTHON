'''PASSWORD_GENERATOR:given input is in the form of names and numbers separated by ','.we have to generate a password such that taking the maximun number from each record which is lesser than the length of the name then fining the letter in the name of the given position,if the digit less then length of name,return 'x'
ex:input:abhisekh:2378,yeah:8998,sinchan:5698
   output:kXa
   '''

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
