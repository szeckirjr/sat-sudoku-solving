#!/usr/bin/env python3
import sys


def encode(i, j, k):
    return 81*(i - 1) + 9*(j - 1) + (k - 1) + 1

def get_clauses(puzzle):
    clauses = []

    # add clauses to enforce the given values in the sudoku puzzle
    for x in range(len(puzzle)):
        if puzzle[x] != 0:
            i = x // 9 + 1
            j = x % 9 + 1
            clauses.append([encode(i, j, puzzle[x])])

    # every cell contains at least one number
    for i in range(1, 10):
        for j in range(1, 10):
            clauses.append([encode(i,j,k) for k in range(1,10)])

    # each number appears at most once in every row
    for i in range(1, 10):
        for k in range(1, 10):
            for j in range(1, 9):
                for l in range(j+1, 10):
                    clauses.append([-encode(i, j, k), -encode(i, l, k)])

    # each number appears at most once in every column
    for j in range(1, 10):
        for k in range(1, 10):
            for i in range(1, 9):
                for l in range(i+1, 10):
                    clauses.append([-encode(i, j, k), -encode(l, j, k)])

    # each number appears at most once in every 3x3 sub-grid
    # TODO

    return clauses

'''
This function opens the file and returns the unsolved sudoku puzzle
into an array. The wildcard values will be always changed to 0. 
'''
def get_puzzle_txt(path):
    try:
        with open(path, 'r') as file:
            puzzle = file.read().strip().replace("\n", "")
            puzzle = [0 if char in [".", "?", "0", "*"] else int(char) for char in puzzle]
        return puzzle

    except Exception as err:
        print(f"Failed to parse from {path}")
        print(err)
        sys.exit(2)


def main(path):
    
    puzzle = get_puzzle_txt(path)
    #print(puzzle)
    clauses = get_clauses(puzzle)
    
    print("p cnf {} {}".format("<# variables>" , len(clauses)))
    for clause in clauses:
        clause.append(0)
        print(*clause)

# This function makes sure only 1 input file is being provided
# Throws error if input is invalid
def parse_args():
    if len(sys.argv) > 2:
        print(f"One argument expected, got {len(sys.argv) - 1}")
        sys.exit(2)
    elif len(sys.argv) < 2:
        print("You must enter a sudoku puzzle in the CL")
        sys.exit(2)

    return sys.argv[1]


if __name__ == "__main__":
    sud = parse_args()
    main(sud)
    
