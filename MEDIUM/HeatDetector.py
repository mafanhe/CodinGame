import sys

__author__ = 'mafanhe'
# 二维的二分法
# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

# w: width of the building.
# h: height of the building.
w, h = [int(i) for i in input().split()]
n = int(input())  # maximum number of turns before game over.
x0, y0 = [int(i) for i in input().split()]
x1, x2, y1, y2 = 0, w-1, 0, h-1

# game loop
while True:
    x, y = x0, y0
    bomb_dir = input()  # the direction of the bombs from batman's current location (U, UR, R, DR, D, DL, L or UL)
    print(bomb_dir, file=sys.stderr)
    print((x1, x2), (y1, y2), file=sys.stderr)
    for b in bomb_dir:
        if b == 'L':
            x2 = x
            x = (x+x1)//2
            if x >= x0:
                x = x0-1
        if b == 'R':
            x1 = x
            x = (x2+x)//2
            if x <= x0:
                x = x0+1
        if b == 'U':
            y2 = y
            y = (y+y1)//2
            if y >= y0:
                y = y0-1
        if b == 'D':
            y1 = y
            y = (y2+y)//2
            if y <= y0:
                y = y0+1

    # Write an action using print
    # To debug: print("Debug messages...", file=sys.stderr)
    print(x, y)
    x0, y0 = x, y
    # the location of the next window Batman should jump to.

