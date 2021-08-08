The input will be a series of graphs in the following format:
N1
Ui1 Uj1
...
%
N2
Ui1 Uj1
...
%
Where Ni is the number of vertices (0 < Ni < 256) and Uih Uil are integers between 1 and Ni indicating that there exists an edge between vertex Uih and Uil. Each graph is terminated with a %.

Example Input:
4
1 2
2 3
2 4
3 4
3 1
%
6
1 2
1 3
1 6
3 2
3 4
5 2
5 4
6 5
6 4
%
Output:
For each test case, output a line that must contain the sequence of vertices that form a Hamiltonian cycle in the form:
Ui1 Ui2 ...

If no such path exists, then output 'None'
Note: To ensure consistent output, make sure you traverse the neighbors of a vertex in sorted order.

Example Output:
1 2 4 3 1
1 2 3 4 5 6 1
