#!/usr/bin/env python3
import collections
import heapq
import sys

# Build Graph
def read_graph(row):
    ''' read input into a list of rows '''
    a={}
    index=0
    for line in sys.stdin:
        a[index]= line.split()
        index+=1
        if index==row:
            break
    return a

def build_graph(input, row, col):
    '''create a graph and calculate weights using dict'''
    g=collections.defaultdict(dict)
    end=[]
    for i in range(0,row):
        for j in range(0,col):
            # find start and end locations, end as a list for multiple
            if input[i][j]=='E':
                end.append((i,j))
            if input[i][j]=='S':
                start=(i,j)

            source=(i,j)
            hh=1
            dd=2

            #if 1 do not connect graph with edges
            s=input[i][j]
            if s=='1':
                continue

            #horizontal
            if i<row-1:
                h= input[i+1][j]
                if h!='1':
                    target_h=(i+1,j)
                    g[source][target_h]=hh
                    g[target_h][source]=hh
            #vertical
            if j<col-1:
                v= input[i][j+1]
                if v != '1':
                    target_v=(i,j+1)
                    g[source][target_v]=hh
                    g[target_v][source]=hh
            #diagonal
            if i<row-1 and j<col-1:
                d=input[i+1][j+1]
                if d!='1':
                    target_d=(i+1, j+1)
                    g[source][target_d]=dd
                    g[target_d][source]=dd

    return g, end, start

# Compute SSSP
def compute_sssp(g, start):
    ''' Use Dijkstra's Algorithm to compute the single-source shortest path '''
    frontier = []
    visited  = {}
    heapq.heappush(frontier, (0, start, start))

    while frontier:
        weight, source, target = heapq.heappop(frontier)
        if target in visited:
            continue
        visited[target] = (source,weight)
        for neighbor, cost in g[target].items():
            heapq.heappush(frontier, (weight + cost, target, neighbor))

    return visited

def reconstruct_path(visited,source, target, col):
    ''' Reconstruct path from source to target '''
    path = []
    curr = target

    while curr != source:
        #get location number and add to path
        location= int(curr[0])*col +int(curr[1])
        path.append(location)
        curr = visited[curr][0]

    location= int(source[0])*col +int(source[1])
    path.append(location)

    return reversed(path)

# Main Execution
def main():
    # Read Graph
    for line in sys.stdin:
        #get row/col
        row, col= map(int,line.rstrip().split())
        #end case
        if row==0 and col==0:
            break
        #create list and build graph
        input = read_graph(row)
        g, end, s= build_graph(input, row, col)

        # Compute SSSP
        v = compute_sssp(g, s)

        mini=100000
        option=-1
        #find best end path
        for i in range(0,len(end)):
            if end[i] not in v:
                continue
            gate=v[end[i]][1]
            if gate<mini:
                mini=gate
                option=i

        if option != -1:
            path=reconstruct_path(v, s,end[option], col)
            print(f'Cost: {mini} Path: {" ".join(str(i) for i in path) }')
        else:
            print(f'Cost: 0 Path: None')

if __name__ == '__main__':
    main()
