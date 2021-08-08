#!/usr/bin/env python3
import sys

 # Class: binary tree node
class Node:
    def __init__(self, d):
        self.data = d
        self.left = None
        self.right = None

#Functions
#calls the tree builder and finds the answer with queue for BFS
def find_max(nums):
    #base
    if not nums:
        return 1,0
    #initialize
    max_level=max_nodes=1
    root= make_tree(nums)

    #make a queue to traverse
    q=[]
    q.append(root)
    level=1

    while q:
        count = len(q)
        #check for max
        if count>max_nodes:
            max_level=level
            max_nodes=count
        level+=1
        while count > 0:
            # Dequeue nodes of current level
            temp = q.pop(0)
            #queue notes in next level
            if temp.left:
                q.append(temp.left)
            if temp.right:
                q.append(temp.right)
            count -= 1

    return max_level, max_nodes

#make tree from preorder and empty nodes
def make_tree(nums):
    #base cases
    if not nums:
        return None
    data = nums.pop(0)
    if data == -1:
        return None
    #recursion
    root = Node(data)
    root.left = make_tree(nums)
    root.right = make_tree(nums)
    

    return root

# Main Execution
def main():
    for line in sys.stdin:
        nums=list(map(int, line.split())) #get list
        max_level, max_nodes= find_max(nums)
        print(f'Level {max_level} has the most nodes: {max_nodes}')

if __name__ == '__main__':
    main()
