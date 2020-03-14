'''SEMIPRIME:A semiprime number is an integer which can be expressed as a product of two distinct primes. For example 15 = 3*5 is a semiprime number but 9 = 3*3 is not .
Given an integer number N, find whether it can be expressed as a sum of two semi-primes or not (not necessarily distinct).
ex:Input:30
   Output:Yes'''
   
 prime1=[]
prime2=[]
semiprime1=[]
semiprime2=[]
last=[]
n=int(input())
for i in range(2,n):
  for j in range(2,i):
    if(i%j==0):
      break
  else:
    prime1.append(i)
    prime2.append(i)
for i in prime1:
  for j in prime2:
    if i!=j and i*j<=n:
      semiprime1.append(i*j)
      semiprime2.append(i*j)
semiprime1.sort()
semiprime2.sort()
for i in semiprime1:
  for j in semiprime2:
    if(i+j<=n):
      if (i+j) not in last:
        last.append(i+j)
last.sort()
if n in last:
  print("Yes",end="")
else:
  print("No",end="")
