import sys

__author__ = 'mafanhe'
# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

# n: the total number of nodes in the level, including the gateways
# l: the number of links
# e: the number of exit gateways

n, l, e = [int(i) for i in input().split()]
links = []
gateway = []

for i in range(l):
    # n1: N1 and N2 defines a link between these nodes
    n1, n2 = [int(j) for j in input().split()]
    links.append({n1, n2})

for i in range(e):
    ei = int(input())  # the index of a gateway node
    gateway.append(ei)

# game loop
while True:
    si = int(input())  # The index of the node on which the Skynet agent is positioned this turn
    # Write an action using print
    # To debug: print("Debug messages...", file=sys.stderr)
    nextLink = [{si, gateway[i]} for i in range(len(gateway))]
    i = 0
    for nextL in nextLink:
        if nextL in links:
            i = 1
            print(nextL.pop(), nextL.pop())
            break

    while i == 0:
        for gate in gateway:
            for line in links:
                if gate in line:
                    print(line.pop(), line.pop())
                    i = 1
                    break
            if i == 1:
                break





