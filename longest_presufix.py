'''LONGEST_PRESUFFIX:given a string s,find the length of the prefix which is also suffix which doesn"t overlap.
ex:input:abcdabc
   output:3
   '''

istring=input()
lenght=len(istring)
half=lenght//2

for i in range(half,0,-1):
    prefix=istring[0:i]
    print(prefix)
    suffix=istring[lenght-i:lenght]
    print(suffix)

    if(prefix==suffix):
        print(len(prefix))
        break

