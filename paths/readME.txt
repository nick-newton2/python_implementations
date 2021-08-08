djikstra.py:
The input will contain multiple test cases. The first line of each test case contains two integers: the number of nodes n (2 <= n <= 25) and the number of edges m (1 <= m <= 25). The next m lines describe the undirected edges, where each edge is given by the numbers of the two nodes connected by it. The nodes are labeled from 0 to n - 1 and have degress of three or less. The network itself is not necessarily connected.
The input will be terminated by two values of 0 for n and m.
Output the length of the longest road.
Uses djikstras algo by making all paths negative and finding the 'minimum'

Ex input:
  3 2
  0 1
  1 2
  15 16
  0 2
  1 2
  2 3
  3 4
  3 5
  4 6
  5 7
  6 8
  7 8
  7 9
  8 10
  9 11
  10 12
  11 12
  10 13
  12 14
  0 0

Ex output:
  2
  12

maze.py:

Each cell in the maze can be one of the following values:
  S: This is the starting cell
  E: This is an ending cell
  0: This is an open cell
  1: This is a closed cell

You can move through an open cell, but not a closed cell. From any open cell, you can move horizontally, vertically, or diagonally to another open or ending cell. Moving horizontally or vertically has a cost of 1, while moving diagonally has a cost of 2.

The maze can vary in size, starting location and multiple end locations. Use Dijkstra's Algorithm to compute the shortest path from the start point to any of the end points and output both the cost and the path itself.


Input: given two numbers, ROWS and COLS, which correspond to the number of rows and columns in the maze. This is followed by the CELLS in the maze where each line represents a row and the cells in the row are separated by spaces. The number of ROWS and COLS will be between 2 and 50 (inclusive).
The input will be terminated by two values of 0 for ROWS and COLS.

Example Input:
4 4
S 0 1 0
0 1 0 0
0 1 0 0
0 0 0 E
4 4
S 0 1 0
0 1 0 0
0 1 0 E
0 E 0 0
4 4
S 0 1 0
0 1 0 0
0 1 E 0
0 E 0 0
0 0

Output: output the cost of the shortest path from the starting cell to any of the ending cells and the cells in the shortest path.

Example Output:
Cost: 6 Path: 0 1 6 10 15
Cost: 4 Path: 0 4 8 13
Cost: 4 Path: 0 1 6 10
Note, as shown above, each cell is identified by a numerical ID based on its position in the maze:
Cell.Id = Cell.Row * Maze.Cols + Cell.Column

There should be spaces between each cell, but not after the last cell in the path.
If there are multiple paths with the same cost, choose the one where the path selects cells with lower numerical IDs from as shown in the third example.

Note, in the first example, we choose the path 0 1 6 10 15 instead of 0 1 6 7 11 15 because from the perspective of 15 node 10 has a lower numerical ID than node 11.

If there are no possible paths from the starting cell to any of the ending cells, then output the following:
Cost: 0 Path: None

city.py:
Input: a series of building locations specified by sets of point locations. The first line of a set denotes the number of points N, followed by N pair of points X Y. The end of the input is denoted when N = 0. N will never be larger than 100.
Example Input:
3
1.0 1.0
2.0 2.0
2.0 4.0
0
Note: assume you can connect buildings directly with a straight-line path.

Output: For each set of building locations, output the minimum total amount of road that must be constructed to connect all the buildings to two decimal places.
Example Output:
3.41

