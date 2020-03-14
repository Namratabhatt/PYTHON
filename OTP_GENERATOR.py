'''OTP_GENERATOR:take an input string from user,square the digits at odd places,then generate an OTP of four digits
ex:input:1234
   output:1491'''
   
istring=input()
length=len(istring)
otp=''
for odd in range(0,length,2):
    otp+=str(int(istring[odd])**2)

print(otp[0:4])
