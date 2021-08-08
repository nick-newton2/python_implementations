#!/usr/bin/env python3
import sys

def main():
    elements = (1, 2, 4)
    bitset   = 0

    # Add elements to bitset
    for i in elements:
        bitset = bitset | 1<<i

    print(bitset)

    # Test for elements in bitset
    for i in range(6):
        if (bitset>>i) & 1:
            print(i)

    for i in range(6):
        if bitset & 1<<i:
            print(i)
    # Remove elements from bitset
    for i in elements:
        bitset = bitset & ~(1<<i)

    # Print contents of bitset
    print(bitset)

if __name__ == '__main__':
    main()
