import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

def str2float(num):
    z,x=num.split(',')
    return float(z)+float(x)/(10**len(x))
        
lon = input()
lat = input()
lon = str2float(lon)
lat = str2float(lat)

n = int(input())

defibs=[]

for i in range(n):
    defib = input()
    defibs.append(defib.split(';'))
    
print(defibs,file=sys.stderr)

result,minDis='',float('Inf')
for defib in defibs:
    d_name=defib[1]
    d_lon=str2float(defib[4])    
    d_lat=str2float(defib[5])
    
    x=(d_lon-lon)*math.cos((d_lat+lat)/2)
    y=d_lat-lat
    distance=math.sqrt(x**2+y**2)*6371
    if distance<minDis:
        minDis=distance
        result=d_name
    
# Write an action using print
# To debug: print("Debug messages...", file=sys.stderr)

print(result)
