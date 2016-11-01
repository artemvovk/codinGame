import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

n = int(input())  # the number of adjacency relations
print("Making %r connections" % n, file=sys.stderr)
nodes = {}
for i in range(n):
    # xi: the ID of a person which is adjacent to yi
    # yi: the ID of a person which is adjacent to xi
    xi, yi = [int(j) for j in input().split()]
    if xi in nodes.keys():
        nodes[xi].append(yi)
        if yi in nodes.keys():
            nodes[yi].append(xi)
        else:
            nodes[yi] = []
            nodes[yi].append(xi)
    else:
        nodes[xi] = []
        nodes[xi].append(yi)
        if yi in nodes.keys():
            nodes[yi].append(xi)
        else:
            nodes[yi] = []
            nodes[yi].append(xi)
    print("Node %r connects to nodes %r" % (xi, nodes[xi]), file=sys.stderr)
        

# Write an action using print
# To debug: print("Debug messages...", file=sys.stderr)
def dropleaves():
    steps = 0
    prevK = -1
    while len(nodes.keys()) > 1:
        for k, v in nodes.copy().items():
            if not v:
                nodes.pop(k)
                continue
            print("Checking %r with neighbors %r" % (k, v), file=sys.stderr)
            if len(v) == 1 and prevK != k:
                print("Removing %r from nodes %r" % (k, v[0]), file=sys.stderr)
                prevK = v[0]
                nodes[v[0]].remove(k)
                nodes.pop(k, v)
        steps += 1
    print("We are left with %r" % (nodes), file=sys.stderr)
    return steps
# The minimal amount of steps required to completely propagate the advertisement
print("%r" % (dropleaves()))

