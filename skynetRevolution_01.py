import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

# n: the total number of nodes in the level, including the gateways
# l: the number of links
# e: the number of exit gateways
n, l, e = [int(i) for i in input().split()]
gates = []
linkArr = []
for i in range(l):
    # n1: N1 and N2 defines a link between these nodes
    n1, n2 = [int(j) for j in input().split()]
    linkArr.append((n1, n2))
for i in range(e):
    ei = int(input())  # the index of a gateway node
    gates.append(ei)
    print ("gateway node at %d" %(ei), file=sys.stderr)
    
#print("link array: %r" %(linkArr), file=sys.stderr)
# recalculate shortest path from si to ei (with closest node value)
# cut off first link from ei to si
# list of all nodes
# starting node = si
# goal node is ei
# arr of links for distance
# look at each link and add it as dist 1 from location
# for arrLink[n][0] find arrLink[n][1] 
# that matches arrLink[j][0] to something closer to ei


def bfs(root, gGates, linkArray):
    gate = gGates
    #print(gate, file=sys.stderr)
    linkLeft = linkArray.copy()
    route = [(root,root)]
    counter = 0
    curNode = root
    while route[counter][0] not in gate and route[counter][1] not in gate:
        for (node1, node2) in linkLeft:
            if curNode == node1 or curNode == node2:
                route.append((node1,node2))
                linkLeft.remove((node1,node2))
                
        #print ("we're at: {0}".format(curNode), file=sys.stderr)
        
        curNode = route[counter][1]
        if counter >= len(route)-1:
            #curNode = route[counter][0]
            counter-=1
        else:
            counter+=1
        #print("route %r with length %r" % (route, len(route)), file=sys.stderr)
        #print("count to %r to gates %r" % (counter, gates), file=sys.stderr)
    #print ("what do we got so far? %r" %([(x,y) for x,y in route if x in gate or y in gate]), file=sys.stderr)
    return ([(x,y) for x,y in route if x in gate or y in gate])
    

# game loop
while True:
    nodeArr = list(range(n))
    si = int(input())  # The index of the node on which the Skynet agent is positioned this turn
    
    # Write an action using print
    # To debug: print("Debug messages...", file=sys.stderr)
    print("agent location: %d" %(si), file=sys.stderr)
    print("num of nodes: %d" %(n), file=sys.stderr)
    print("link array: %r" %(len(linkArr)), file=sys.stderr)

    ans = bfs(si, gates, linkArr)[0]
    linkArr.remove(ans)
    # Example: 0 1 are the indices of the nodes you wish to sever the link between
    print (' '.join(map(str, ans)))

