#!/usr/bin/env python3
import sys

#read in input grid
def read_grid(n):
    grid = [[0 for _ in range(n + 1)]]  # Pad grid
    for _ in range(n):
        grid.append([0] + list(map(int, sys.stdin.readline().split())))
    return grid

#fill in the table of occurences
def avoid(grid, n):
    # 1. Initialize table
    table = [[0 for _ in range(n + 1)] for _ in range(n + 1)]

    for row in range(1, n + 1):
        for col in range(1, n + 1):
            #cases to avoid 0 padding on min
            if row==1 and col>1:
                value = table[row][col-1]
            elif col==1 and row>1:
                value = table[row-1][col]
            else:
                value = min(
                    table[row][col - 1],
                    table[row - 1][col],
                    table[row-1][col-1]
                )
            table[row][col] = grid[row][col] + value

    return table

#find the path taken
def find_path(grid, n, table):
    # Reconstruct the path by going from the end to the beginning.
    path = []
    r, c = n, n

    while r > 0 and c > 0:
        # Add current position to path
        path.append(grid[r][c])

        # Consider which path we took based on the values in the table
        if table[r][c] - grid[r][c] == table[r][c-1]:
            c-=1
        elif table[r][c] - grid[r][c] == table[r-1][c]:
            r-=1
        else:
            r-=1
            c-=1
    # Reverse path since we want to go from start to end
    path.reverse()
    return path

def main():
    while True:
        n = int(sys.stdin.readline())
        if n==0:
            break

        grid  = read_grid(n)
        table= avoid(grid, n)
        print(table[n][n])
        path=find_path(grid, n, table)
        print(*path, sep = " ")

# Main execution
if __name__ == '__main__':
    main()
