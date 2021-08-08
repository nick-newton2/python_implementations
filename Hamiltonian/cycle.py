#!/usr/bin/env python3
import sys
import collections


#read from stdin
def read_graph():
    # Store edges and degrees
    graph = collections.defaultdict(set)
    line= sys.stdin.readline().rstrip()

    #build until sentinel reached
    while line != '%':
        a, b = map(int, line.split())
        graph[a].add(b)
        graph[b].add(a)
        line= sys.stdin.readline().rstrip()

    return graph

def find_circuit(graph, num, visited, path):
    ''' Recursive DFS traversal '''
    #base
    if not path:
        path.append(1)

    # max length
    if len(path)== num +1:
        #hamiltonian if reached start again (end=start)
        if path[-1]==1:
            return path
        else:
            return -1

    #check target options
    source= path[-1]
    for target in graph[source]:
        #next target if already visited or gets circuit before path len reached
        if (target in visited) or (target==1 and len(path)!= num):
            continue

        #update
        visited[target]=1
        path.append(target)

        #Recursive
        if find_circuit(graph, num, visited, path):
            return path
        #pop off if the path doesnt work
        path.pop(-1)
        visited.pop(target)

    # No circuit found, so return nothing
    return []

def main():
    for line in sys.stdin:

        num= int(line)
        #read in stdin and find path
        graph= read_graph()
        path= find_circuit(graph, num, {},[])

        #display
        if path:
            print(*path)
        else:
            print('None')

if __name__ == '__main__':
    main()
