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

