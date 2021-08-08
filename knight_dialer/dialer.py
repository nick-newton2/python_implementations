#!/usr/bin/env python3
import sys

#Global
#Hop Options Dictionary
KNIGHT = {
    1: (6, 8),
    2: (7, 9),
    3: (4, 8),
    4: (0, 3, 9),
    6: (0, 1, 7),
    7: (2, 6),
    8: (1, 3),
    9: (2, 4),
    0: (4, 6)
}

# Functions
#use a generator to find the combinations
def find_move_rec(start, hops, moves):
    #append moves each time
    moves+= str(start)

    #base case, check if need a hop or if at 5 (no options)
    if len(moves)==hops or start==5:
        yield moves
    #recursive, start becomes next option in for loop
    else:
        for option in KNIGHT[start]:
            yield from find_move_rec(option, hops, moves)

# Main Execution
def main():
    count=0 #keep track of final new line
    for line in sys.stdin:
        #only print if there is a previous test, but only print when enter loop
        if count>0:
            print()
        count+=1
        start, hops = map(int, line.strip().split()) #input
        for move in find_move_rec(start, hops, ''):
            if hops==0: #special case 1, no hops
                break
            if start==5 and hops!=1: #special case 2, 5 multiple hops
                break
            print(move) #standard print from function

if __name__ == '__main__':
    main()
