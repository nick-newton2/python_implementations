#!/usr/bin/env python3
import sys

#find the index of the target number
def find_index(nums, target):
    start=0
    end=len(nums)-1

    #use binary search tree concept
    while(start<=end):
        middle= (start+end)//2
        #target found
        if nums[middle]==target:
            return middle

        if nums[start]<=nums[middle]:
            if(nums[start]<=target and target<nums[middle]): #left of pivot
                end=middle-1 #move right side in
            else:
                start=middle+1 #move left side in
        else:
            if(nums[middle]<target and target <=nums[end]): #between middle and end
                start=middle+1
            else:
                end=middle-1
    #no index
    return -2

# Main execution
def main():
    for line in sys.stdin:
        nums= list(map(int, line.rstrip().split()))
        target= int(sys.stdin.readline())
        index= find_index(nums, target)
        if index == -2:
            print(f'{target} was not found')
        else:
            print(f'{target} found at index {index}')

if __name__ == '__main__':
    main()
