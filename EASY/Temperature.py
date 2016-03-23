import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

n = int(input())  # the number of temperatures to analyse
temps = input()  # the n temperatures expressed as integers ranging from -273 to 5526

# Write an action using print
# To debug: print("Debug messages...", file=sys.stderr)
print(n,temps, file=sys.stderr)
if n==0:
    print(0)
else:

    temps=[int(x)for x in temps.split()]
    closest=temps[0]
    for i in range(n):
        if abs(temps[i])<abs(closest):
            closest=temps[i]
        elif abs(temps[i])==abs(closest) and temps[i]>0:
            closest=temps[i]

    print(closest)