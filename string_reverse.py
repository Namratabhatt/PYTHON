string = input()
arr = []
op = ""
for x in string[::-1]:
    if x.isalpha():
        arr.append(x)
i = 0
for x in string:
    if x.isalpha():
        op = op + arr[i]
        i+=1
    else:
        op = op + x
print(op)