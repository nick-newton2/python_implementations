BST.py:
Using divide and conquer O(nlogn) runtime
Given a series of lines, where each line contain a sequence of integers in ascending order, output the binary search tree constructed from the sequence of integers by displaying all the nodes in the BST level by level

  Ex input:
    0 1 2 3 4 5 6
  Ex output:
    3
    1 5
    0 2 4 6
    
BFS.py
Given a tree input in breadth-first order, and a decimal target, find the number of occurences the binary target has on the tree
  Ex input:
    3 110010000111111
    9 110010000111111
    2 110010000111111
  Ex output:
    Paths that form 3 in binary (11): 4
    Paths that form 9 in binary (1001): 4
    Paths that form 2 in binary (10): 2
    
level_order.py
Given a series of workflows represented by binary trees in pre-order traversal order, determine where it has its maximum concurrency by finding the level with the most nodes in the binary tree and output a message

Ex input:
  2 1 4 -1 -1 6 5 -1 -1 -1 3 -1 8 -1 -1
  Note, the -1 in the input denotes that there is no Node there (ie. NULL).

Ex output:
  Level 3 has the most nodes: 3
  Note, if there are multiple levels with the maximum number of nodes, then choose the level with the highest value (ie. further down the tree).
