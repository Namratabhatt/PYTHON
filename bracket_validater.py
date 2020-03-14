'''BRACKET_VALIDATOR: compute the position at which the brackets loose its completeness
ex:input:[][
   output:4'''

def validator(string):
    count=0
    list=[]
    
    for b in string:
        if(b=='[' or b=='{' or b=='()'):
            list.append(b)
            count+=1
            continue

        if(len(list)==0):
            return count+1
        
        x=list.pop()
        if(b==']' and x=='['):
            count+=1
        elif(b=='}' and x=='{'):
            count+=1
        elif(b==')' and x=='('):
            count+=1
        else:
            return count+1
    if(len(list)==0):
        return 0
    else:
        return count+1
        
string=input()
print(validator(string))
