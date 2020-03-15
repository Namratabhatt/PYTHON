n=int(input())

divisor=[1]
i=2
while(i*i<=n):
    if(n%i==0):
        divisor.append(i)
        divisor.append(n//i)
    i+=1

summ=sum(divisor)
if(n==1 or summ!=n):
    print("no")
else:
    print("yes")
