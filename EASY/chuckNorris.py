import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

message = input()

# Write an action using print
# To debug: print("Debug messages...", file=sys.stderr)
print(message,file=sys.stderr)

binms=""

for m in str(message):
    binm=bin(ord(m)).replace('0b','')
    if len(binm)<7:
        binm='0'+binm
    binms+=binm

print(binms,file=sys.stderr)
result=""
i,j=0,0

while i<len(binms) and j<len(binms):
    if binms[i]=='1':
        result+=' 0 '
    else:
        result+=' 00 '
    j=i
    while j<len(binms):
        if binms[j]==binms[i]:
            result+='0'
            j+=1
        else:
            i=j
            break
    if i!=j:
        i+=1

print(result.strip())
