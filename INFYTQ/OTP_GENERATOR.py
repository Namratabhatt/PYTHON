istring=input()
length=len(istring)
otp=''
for odd in range(0,length,2):
    otp+=str(int(istring[odd])**2)

print(otp[0:4])
