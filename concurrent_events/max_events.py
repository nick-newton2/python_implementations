#!/usr/bin/env python3
import sys

#read in values from stdin based on rows (events)
def read_times(events):
    times=[]
    for __ in range(events):
        time=list(map(int, sys.stdin.readline().split()))
        #add boolian concept to know if start or end time
        times.append([time[0], "begin"])
        times.append([time[1], "end"])
    #sort by time, begin already maintains sorted order
    times.sort()
    return times

def find_concur(times):
    maximum=0
    current=0

    for time in times:
        if time[1] == "begin":
            current+=1 #append concurrent current events
            maximum=max(current,maximum)
        else: #event ending
            current-=1
    return maximum

def main():
    count = 0
    for line in sys.stdin:
        events = line.rstrip()
        events=int(events)
        count +=1
        times= read_times(events)
        concur= find_concur(times)
        print(f"{count}. Maximum number of concurrent events is {concur}")

if __name__ == '__main__':
    main()
