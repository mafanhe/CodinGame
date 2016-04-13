import sys
import math

# Don't let the machines win. You are humanity's last hope...

width = int(input())  # the number of cells on the X axis
height = int(input())  # the number of cells on the Y axis
cells=[]
for i in range(height):
    line = input()  # width characters, each either 0 or .
    cells.append(line)
# Write an action using print
# To debug: print("Debug messages...", file=sys.stderr)

# Three coordinates: a node, its right neighbor, its bottom neighbor

for i in range(len(cells)):
    for j in range(len(cells[0])):
        if cells[i][j]!='.':
            result="%d %d" % (j,i)
            if j+1<len(cells[0]):
                for k in range(j+1,len(cells[0])):
                    if cells[i][k]!='.':
                        result+=" %d %d" % (k,i)
                        break
                    elif k==len(cells[0])-1:
                        result+=" -1 -1"
                        break
            else:
                result+=" -1 -1"
            if i+1<len(cells):
                for l in range(i+1,len(cells)):
                    if cells[l][j]!='.':
                        result+=" %d %d" % (j,l)
                        break
                    elif l==len(cells)-1:
                        result+=" -1 -1"
                        break
            else:
                result+=" -1 -1"
            print(result)

