#!/usr/bin/env python3
import collections
import heapq
import sys
import math

#caluclate from distance formula
def calc_dist(a, b):
    return math.sqrt((a[0]-b[0])**2 + (a[1]-b[1])**2)

# Build Graph of points from input
def read_graph(num):
    ''' Read in undirected graph '''
    #make points dict with tuple float coordinates
    points={}
    for i in range(0,num):
        x, y = map(float, sys.stdin.readline().rstrip().split())
        points[i]=(x,y)
    return points

#save the distances between points to dict g
def find_dist(points):
    g = collections.defaultdict(dict)
    for i in points:
        for j in points:
            dist=calc_dist(points[i], points[j])
            g[i][j]=dist
            g[j][i]=dist
    return g

# Compute MST
def compute_mst(g):
    frontier= []
    visited= {}
    start= list(g.keys())[0]

    heapq.heappush(frontier, (0, start, start))

    while frontier:
        weight, source, target = heapq.heappop(frontier)

        if target in visited:
            continue

        visited[target] = source

        for neighbor, cost in g[target].items():
            heapq.heappush(frontier, (cost, target, neighbor))

    return visited

def find_sum(g, m):
    e = sorted((min(s, t), max(s, t)) for s, t in m.items() if s != t)
    return sum(g[s][t] for s, t in e)

# Main Execution
def main():
    for line in sys.stdin:
        num=int(line)
        if num==0:
            break
        #read graph
        points = read_graph(num)
        #print(points)
        g=find_dist(points)

        # Compute MST
        m = compute_mst(g)

        # Print
        total=find_sum(g, m)
        print(f'{total:.2f}')

if __name__ == '__main__':
    main()
