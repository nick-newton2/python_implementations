#!/usr/bin/env python3
import collections
import heapq
import sys

# Build Graph, m keeps track of reading input
def read_graph(m):
    ''' Read in undirected graph '''
    g = collections.defaultdict(dict)
    #for i in range(m):
    for line in sys.stdin:
        source, target= line.split()
        weight = -1
        g[source][target] = int(weight)
        g[target][source] = int(weight)
        m-=1
        if m==0: #stop appending dictionary
            return g
    return g

# Compute SSSP
def compute_sssp(g, start):
    ''' Use Dijkstra's Algorithm to compute the longest path '''
    frontier = []
    visited  = {}
    heapq.heappush(frontier, (0, start, start))
    local_max=abs_max=0
    while frontier:
        weight, source, target = heapq.heappop(frontier)

        #visited needs to be tracking edges (boht ways) not nodes
        edge=(source, target)
        edge_r=(target, source)
        if edge in visited or edge_r in visited:
            continue

        #keep track of max
        local_max=weight*(-1)
        abs_max=max(local_max, abs_max)

        #update visited
        visited[edge] = (source,local_max)
        visited[edge_r] = (source,local_max)

        for neighbor, cost in g[target].items():
            heapq.heappush(frontier, (weight + cost, target, neighbor))

    return abs_max

# Main Execution
def main():
    for line in sys.stdin:
        n, m = map(int, line.split())
        maximum=0
        #end case
        if n==0 and m==0:
            break

        # Read Graph
        g = read_graph(m)

        # Compute SSSP
        for i, n in enumerate(g):
            v= compute_sssp(g, n)
            maximum=max(maximum, v)
        print(maximum)

if __name__ == '__main__':
    main()
