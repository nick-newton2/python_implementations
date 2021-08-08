#!/usr/bin/env python3
import sys

# Function
#count total solutions
def count_solutions(n, cache={}):
    #initialize variable
    count=0

    #base case
    if n<1 :
        return 1

    #see if value cached or calculate recursively for each number
    if n not in cache:
        if n>=1:
            count+= 2*count_solutions(n-1, cache) #4 and 1 are same
        if n>=2:
            count+=count_solutions(n-2, cache)
        if n>=3:
            count+=count_solutions(n-3, cache)
        cache[n]=count
    else: #if value already found, return it
        return cache[n]

    #return final count
    return count


def main():
    for n in map(int, sys.stdin):
        print(count_solutions(n))

# Main execution
if __name__ == '__main__':
    main()
