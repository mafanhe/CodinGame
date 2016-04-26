import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

n = int(input())  # the number of adjacency relations
rela={}
for i in range(n):
    # xi: the ID of a person which is adjacent to yi
    # yi: the ID of a person which is adjacent to xi
    xi, yi = [int(j) for j in input().split()]
    if rela.get(xi)==None:
        rela[xi]=[yi] 
    else:
        rela[xi].append(yi)
    if rela.get(yi)==None:
        rela[yi]=[xi] 
    else:
        rela[yi].append(xi)

print(rela,file=sys.stderr)  
b= sorted(rela.items(), key=lambda d: len(d[1]),reverse=True)

# Write an action using print
# To debug: print("Debug messages...", file=sys.stderr)


# The minimal amount of steps required to completely propagate the advertisement
min_hour=100000
for i in b:
    cur=[i[0]]
    hour=0
    visited=[i[0]]
    # print("start:",i,file=sys.stderr)
    while len(visited)<=n:
        # curr=[]
        length=len(cur)
        while length>0:
            cu=cur.pop(0)
            for rel in rela[cu]:
                if rel not in visited:
                    cur.append(rel)
                    visited.append(rel)
            length-=1
        hour+=1
        print(cur,visited,file=sys.stderr)
        if hour>=min_hour:
            break
    print(i[0],hour,file=sys.stderr)
    min_hour=hour if hour<min_hour else min_hour

print(min_hour) 
            
        