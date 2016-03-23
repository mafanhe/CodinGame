import sys
import math

#没有过最后一个检查点
# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

l = int(input())
h = int(input())
t = input()
rows=[]
for i in range(h):
    row = input()
    rows.append(list(row))

print (t, file=sys.stderr)

for i in range(h):
    for x in t:
        if 65<=ord(x.upper())<=90:
            num=(ord(x.upper())-65)*4
            for j in range(num,num+4):
                print (rows[i][j],end="")
        else:
            for j in range(26*4,27*4):
                print (rows[i][j],end="")
    print("")


