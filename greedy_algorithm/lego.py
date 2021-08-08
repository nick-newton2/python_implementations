#!/usr/bin/env python3
import sys

#find the rows using greedy algorithm
def find_rows(brick_list):
    rows=0
    #start from location 3 in list (4 pieces)
    for brick_size in reversed(range(4)):
        #count biggest piece rows first in while loop
        while brick_list[brick_size]>0:
            rows += 1 #add a row
            brick_list[brick_size]-=1

            # size 3
            if(brick_size==2 and brick_list[0]>0):
                brick_list[0]-=1 #subtract from single piece

            #size 2
            if brick_size==1:
                if brick_list[1]>0:
                    brick_list[1] -= 1 #subtract additional 2 piece
                else:
                    brick_list[0]-=2 #subtract 2 single pieces

            #size 1
            if brick_size==0:
                brick_list[0] -=3 #subtract additional single pieces
    return rows

def main():
    for line in sys.stdin:
        brick_list = list(map(int, line.strip().split())) #input list read
        rows = find_rows(brick_list)
        print(rows) #display

if __name__ == '__main__':
    main()
