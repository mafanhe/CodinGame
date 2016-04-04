import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.
pis=[]
n = int(input())
for i in range(n):
    pi = int(input())
    pis.append(pi)

# Write an action using print
# To debug: print("Debug messages...", file=sys.stderr)
pis.sort()

mind=10000000
for i in range(len(pis)-1):
    d = abs(pis[i]-pis[i+1])
    if d<mind:
        mind=d
print(pis,file=sys.stderr)
print (mind)