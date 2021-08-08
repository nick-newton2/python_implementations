#!/usr/bin/env python3
import sys

# Function
def count_mask(mask, bitset):
    count=0
    i=1
	#include leading 0s
    new_mask=mask.zfill(4)
    bitset=bitset.zfill(32)

	#find matches
    bits= len(new_mask)
    while i < (len(bitset)-bits)+2:
        end=len(bitset)-i
        start=end-bits+1
        temp_bit=bitset[start:end+1]
        i += 1
        if temp_bit==new_mask:
            count += 1
    return count

def read_input(line):
    mask, bitset = line.strip().split()
    mask = int(mask, 16)
    bitset= int(bitset)
    mask = format(mask, 'b')
    bitset= format(bitset, 'b')
    return mask, bitset

# Main execution
def main():
    for index, line in enumerate(sys.stdin, 1):
        mask, bitset= read_input(line)
        count= count_mask(mask, bitset)
        print(f'{index}. {int(bitset, 2)} contains 0x{int(mask, 2):X} {count} times')

if __name__ == '__main__':
    main()
