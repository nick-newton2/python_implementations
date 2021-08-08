#!/usr/bin/env python3
import sys

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

def printRoute(stack, root, answer, target):
    if root == None:
        return
    if root.data ==0:
        return

    # append node to the path array
    stack.append(root.data)
    if((root.left == None and root.right == None) or
    ((root.left!= None and root.left.data == 0) and (root.right!= None and root.right.data == 0)) or
    ((root.left!= None and root.left.data == 0) and root.right == None) or
    (root.left == None and (root.right!= None and root.right.data == 0))):
        # check if the path sums to target and save to answer
        if sum(stack)==target:
            answer.append(tuple(stack))
    # otherwise try both subtrees
    if root.left!=0:
        printRoute(stack, root.left, answer, target)
    if root.right!=0:
        printRoute(stack, root.right, answer, target)
    stack.pop()

# Main Execution
def main():
    for line in sys.stdin:
        root=None
        target= int(line)
        values= list(map(int, sys.stdin.readline().split()))

        #create tree
        root = level_order_BST(values, root, 0, len(values))

        #find the correct paths
        answer=[]
        printRoute([], root, answer, target)
        answer.sort()

        #display
        if len(answer)==0:
            print()
        else:
            for ans in answer:
                ans= ', '.join(str(i) for i in ans)
                print(f'{target}: {ans}')

if __name__ == '__main__':
    main()
