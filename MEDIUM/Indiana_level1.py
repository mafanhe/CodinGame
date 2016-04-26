__author__ = 'mafanhe'

import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

# w: number of columns.
# h: number of rows.
w, h = [int(i) for i in input().split()]
lines={}
for i in range(h):
    line = input()  # represents a line in the grid and contains W integers. Each integer represents one room of a given type.
    colum = line.split(' ')
    for j in range(w):
        lines[(j,i)]=colum[j]

ex = int(input())  # the coordinate along the X axis of the exit (not useful for this first mission, but must be read).
print(lines,file=sys.stderr)
# game loop
while True:
    xi, yi, pos = input().split()
    xi = int(xi)
    yi = int(yi)
    print(lines[(xi,yi)],file=sys.stderr)
    if lines[(xi,yi)] in ('1','3','7','8','9','12','13') :
        print(xi,yi+1)
    elif lines[(xi,yi)] in ('2','6'):
        if pos=="LEFT":
            print(xi+1,yi)
        else:
            print(xi-1,yi)
    elif lines[(xi,yi)] in ('4','10'):
        if pos=="TOP":
            print(xi-1,yi)
        else:
            print(xi,yi+1)
    elif lines[(xi,yi)] in ('5','11'):
        if pos=="TOP":
            print(xi+1,yi)
        else:
            print(xi,yi+1)
    else:
        if pos=="TOP":
            print(xi,yi+1)
        elif pos=="LEFT":
            print(xi+1,yi)
        else:
            print(xi-1,yi)
    # Write an action using print
    # To debug: print("Debug messages...", file=sys.stderr)


    # One line containing the X Y coordinates of the room in which you believe Indy will be on the next turn.

