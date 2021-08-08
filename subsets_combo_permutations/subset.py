#!/usr/bin/env python3
import sys
import itertools

def findsubsets(s, n):
    count=0
    x= list(itertools.combinations(s, n))
    for tupp in x:
        if sum(tupp) % 3 == 0:
            count +=1
    return count
    
def main():
    s = {0, 1, 2, 3, 4, 5, 6, 7, 8, 9}
    sum_a=0

    for i in range(0,11):
        sum_a += findsubsets(s, i)
    print(sum_a)



if __name__ == '__main__':
    main()
