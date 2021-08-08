#!/usr/bin/env python3
import sys
import collections

### CHALLENGE 19
Graph = collections.namedtuple('Graph', 'edges degrees')

#read from stdin
def read_graph():
    # Store edges and degrees
    edges = collections.defaultdict(set)
    degrees = collections.defaultdict(int)

    for line in sys.stdin:
        nums=[]
        for num in line.rstrip():
            nums.append(num)

        for i in range(len(nums)-1):
            source = nums[i]
            target = nums[i+1]

            #check
            if target in edges[source]:
                continue

            #update graph
            edges[source].add(target)
            degrees[target] += 1
            degrees[source]

    return Graph(edges, degrees)


# Topological Sort
def topological_sort(graph):
    frontier = [v for v, d in graph.degrees.items() if d == 0]
    visited  = []

    while frontier:
        vertex = frontier.pop()
        visited.append(vertex)

        for neighbor in graph.edges[vertex]:
            graph.degrees[neighbor] -= 1
            if graph.degrees[neighbor] == 0:
                frontier.append(neighbor)
    return visited

def main():
    #read in input and do topo sort
    graph= read_graph()
    vertices= topological_sort(graph)

    #display
    if len(vertices) == len(graph.degrees):
        print(''.join(vertices))
    else:
        print('There is a cycle')

if __name__ == '__main__':
    main()
