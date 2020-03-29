'''
INPUT A MATRIX.CHECK IF DO WE GET THE SAME NUMBER CONSECUTIVELY
AT LEAST4 TIMES IN ANY FASHION(VERTICAL,HORIZONTAL,DIAGONAL).
RECORD THOSE SETS.IF WE DO GET MULTIPLE THEN PRINT THE MINIMUN OF THEM
EX:I/P:1 3 3 3 3 9
       1 6 9 2 3 9
       1 2 2 5 4 9
       2 2 4 5 7 9
       2 4 5 6 7 2
       1 2 3 4 5 6
   O/P:2
'''
row=6
col=6
matrix=[]
final=[]
for r in range(6):
    rows=list(map(int,input().split(" ")))
    matrix.append(rows)

for r in range(row):
    for c in range(col):
        if(c<col-3):
            if(matrix[r][c]==matrix[r][c+1]==matrix[r][c+2]==matrix[r][c+3]):
                final.append(matrix[r][c])
        if(r<row-3):
            if(matrix[r][c]==matrix[r+1][c]==matrix[r+2][c]==matrix[r+3][c]):
                final.append(matrix[r][c])
        if(c<col-3 and r>=3):
            if(matrix[r][c]==matrix[r-1][c+1]==matrix[r-2][c+2]==matrix[r-3][c+3]):
                final.append(matrix[r][c])
        if(r<row-3 and c<col-3):
            if(matrix[r][c]==matrix[r+1][c+1]==matrix[r+2][c+2]==matrix[r+3][c+3]):
                final.append(matrix[r][c])

if(len(final)==0):
    print("-1")
else:
    print(min(final))      