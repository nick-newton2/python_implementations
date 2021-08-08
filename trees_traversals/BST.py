#!/usr/bin/env python3
import sys
import collections


# Class: binary tree node
class Node:
    def __init__(self, d):
        self.data = d
        self.left = None
        self.right = None

#Functions
#get BST from list input
def list_to_BST(nums):
    #base
    if not nums:
        return None

    # find middle (divide) and make it root
    mid = (len(nums)) // 2
    root = Node(nums[mid])

    # left and right subtrees
    root.left = list_to_BST(nums[:mid])
    root.right = list_to_BST(nums[mid+1:])

    return root

#print output
def print_level_order(root):

    # Base case
    if root is None:
        return

    # Create a queue for BFS
    q = []
    #initialize
    q.append(root)

    while q:
        count = len(q)

        while count > 0:
            # Dequeue nodes of current level
            temp = q.pop(0)
            if count>1:
                print(temp.data, end = ' ')
            else: #the final number in level, no space
                print(temp.data)
            #queue notes in next level
            if temp.left:
                q.append(temp.left)
            if temp.right:
                q.append(temp.right)

            count -= 1

# Main Execution
def main():
    for line in sys.stdin:
        nums=list(map(int, line.rstrip().split())) #get list
        root = list_to_BST(nums) #create tree
        print_level_order(root) #print tree

if __name__ == '__main__':
    main()
