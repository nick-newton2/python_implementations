Uses Edmonds-Karp algorothm to calculate max flow in a flow network

Given a series of networks. The first line of the input specifies the number of nodes in the network (2 <= n <= 100). This is followed by a line that contains the source, target, and total number of connections. After this, you will be given the specification for each connection in the form of node 1, node 2, and capacity.
The final network will specify 0 nodes and should not be displayed.
Note: All connections are bi-directional, and there may be multiple connections between a pair of nodes (but a node cannot connect to itself).

Example Input:
4
1 4 5
1 2 20
1 3 10
2 3 5
2 4 10
3 4 20
0

Output: for each network configuration, print the network number (starting with 1) and the maximum bandwidth as shown below.

Example Output:
Network 1: Bandwidth is 25.
