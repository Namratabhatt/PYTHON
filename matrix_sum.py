'''FIND THE ALL POSSIBLE 2*2 MATRIX WITHIN A MATRIX IN WHICH 
EACH ELEMENT OF THE 2*2 MATRIX SHOULD BE DDIVISIBLE BY SUM OF ITS DIGITS
EX:
I/P:42  54  2
    30  24  27
    180 190 40
    11  121 13
O/P:
42 54
30 24

54 2
24 27

30 24
180 190

24 27
190 40
'''

def isdivisible(n):
    s=sum(list(map(int,str(n))))
    if(n%s==0):
        return True
    else:
        return False


matrix=[]
row=int(input())
for i in range(row):
    matrix.append(list(map(int,input().split(" "))))
col=len(matrix[0])

for r in range(row-1):
    for c in range(col-1):
        if(isdivisible(matrix[r][c]) and isdivisible(matrix[r][c+1]) and isdivisible(matrix[r+1][c]) and isdivisible(matrix[r+1][c+1])):
            print(matrix[r][c],matrix[r][c+1])
            print(matrix[r+1][c],matrix[r+1][c+1])

