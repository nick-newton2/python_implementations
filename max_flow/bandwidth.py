#!/usr/bin/env python3
import sys
import collections
import heapq

def read_graph(connections):
    graph= collections.defaultdict(dict)
    for i in range(connections):
        a, b, capacity= map(int, sys.stdin.readline().rstrip().split())

        if a in graph[b] and b in graph[a]:
            graph[a][b]+= capacity
            graph[b][a]+= capacity
        else:
            graph[a][b]= capacity
            graph[b][a]= capacity

    return graph

#from Edmonds Karp and BFS traversal
def find_max_flow(nodes, source, target, graph):
    #Initialize
    max_flow=0

    #initial BFS
    temp_flow, parents= bfs(source, target, graph, parents={})

    #iterate through BFS until no more paths
    while temp_flow>0:
        #Update
        max_flow += temp_flow
        curr= target
        # go backwards on path and decrease flow by smallest (temp_flow)
        while curr != source:
            prev= parents[curr]
            graph[prev][curr]-= temp_flow
            graph[curr][prev]-= temp_flow
            curr=prev
        #continue bfs until no temp_flow
        temp_flow, parents= bfs(source, target, graph, parents={})
    return max_flow

def bfs(source, target, graph, parents):
    #set root
    parents[source]= -1

    #setup queue for BFS
    q=[]
    heapq.heappush(q, (10000, source))

    #go through paths to target
    while q:
        temp_flow, curr= heapq.heappop(q)
        for next in graph[curr]:
            #no parent and positive flow
            if graph[curr][next]>0 and next not in parents:
                #Update
                parents[next]=curr
                temp_flow=min(temp_flow, graph[curr][next])
                #return when find target
                if next == target:
                    return temp_flow, parents
                #update
                heapq.heappush(q, (temp_flow, next))
    #else, no paths
    return 0, parents

def main():
    for index, line in enumerate(sys.stdin, 1):
        #get nodes and check
        nodes= int(line)
        if nodes==0:
            break
        #get initial source/sink and connections
        source, target, connections= map(int, sys.stdin.readline().rstrip().split())
        #build graph
        graph= read_graph(connections)

        #find and display
        maximum= find_max_flow(nodes, source, target, graph)
        print(f'Network {index}: Bandwidth is {maximum}.')

if __name__ == '__main__':
    main()
