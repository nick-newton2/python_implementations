#!/usr/bin/env python3
import sys

ready=[False]*10000
value=[10000]*10000

def count(x):
    coins = [1, 3, 4]
    if x<0:
        return 10000
    if x==0:
        return 0
    if ready[x]:
        return value[x]
    best=1000000
    for c in coins:
        best= min(best, count(x-c)+1)
    value[x]= best
    ready[x]=True
    return best

def main():

    print(count(17))
    print(count(33))
    print(count(64))
    print(count(71))
    print(count(99))

if __name__ == '__main__':
    main()
