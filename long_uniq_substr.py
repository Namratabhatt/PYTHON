'''given a string, find the longest substring  of lenght greater than 3 with unique characters which is case insensitive
ex:ip:aabcbc
   op:abc
   '''


istring=input()
lenght=len(istring)
unique=''

for i in range(lenght):
    substring=istring[i]
    for j in range(i+1,lenght):
        substring+=istring[j]
        len_sub=len(substring)
        if(len_sub>=3 and len(set(substring))==len_sub):
            if(len(unique)<len_sub):
                unique=substring

if(len(unique)==0):
    print("-1")
else:
    print(unique)
