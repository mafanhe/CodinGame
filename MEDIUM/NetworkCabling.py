__author__ = 'mafanhe'
import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

n = int(input())
print(n,file=sys.stderr)

minx=float('inf')
maxx=-float('inf')
sumy=0
linesy=[]
for i in range(n):
    x, y = [int(j) for j in input().split()]
    if x<minx:
        minx=x
    if x>maxx:
        maxx=x
    sumy+=y
    linesy.append(y)

avgy = sumy/n
smallergap=float('inf')
closesty=0
for y in linesy:
    gapy=abs(y-avgy)
    if gapy<smallergap:
        smallergap=gapy
        closesty=y

minsum=0
for y in linesy:
    minsum+=abs(y-closesty)

print(minsum+maxx-minx)


