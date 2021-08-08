#!/usr/bin/env python3
import sys
import math

# Class: binary tree node
class Node:
    def __init__(self, d):
        self.data = d
        self.left = None
        self.right = None

#Functions
#get BST from list input
def level_order_BST(arr, root, i, n):
    # Base case for recursion
    if i < n:
        temp = Node(arr[i])
        root = temp
        # insert left child
        root.left = level_order_BST(arr, root.left, 2 * i + 1, n)
        # insert right child
        root.right = level_order_BST(arr, root.right, 2 * i + 2, n)
    return root

#finds matches at specified target length, returns to count_target
def get_key(root, length, key, target):
    #base cases
    if not root:
        return 0
    if length==0:
        return 0
    count=0
    #add list to compare
    key.append(root.data)
    #recursion
    if len(key) < len(target):
        left_count=get_key(root.left, length-1, key, target)
        right_count=get_key(root.right, length-1, key, target)
        key.pop(-1)
        return left_count+right_count
    #check match
    if key==target:
        count=1
    else:
        count=0
    key.pop(-1)

    return count+get_key(root.left, length-1, key, target)+get_key(root.right, length-1, key, target)

#reads through tree and finds total count
def count_target(root, target, height):
    #base
    if not root:
        return 0
    if height==0:
        return 0
    length=len(target)
    if height< length:
        return 0

    key=[]
    #get count for this subtree
    count=get_key(root, length, key, target)
    #recursion for subtrees
    left_count= count_target(root.left, target, height-1)
    right_count= count_target(root.right, target, height-1)
    #print(f'left, right: {left_count} {right_count}') ######
    return count + left_count + right_count

# Main Execution
def main():
    for line in sys.stdin:
        root=None
        target, nums= line.split()

        target_old=target
        target=format(int(target), 'b')
        targets=" ".join(target)
        targets=list(map(int, targets.rstrip().split()))

        nums=" ".join(nums)
        nums=list(map(int, nums.rstrip().split())) #get list

        length=len(nums)
        height=math.floor(math.log(length,2))+1

        root = level_order_BST(nums, root, 0, len(nums)) #create tree
        count= count_target(root, targets, height)
        print(f'Paths that form {target_old} in binary ({target}): {count}')

if __name__ == '__main__':
    main()
