#!/usr/bin/env python3

# STDIN must be in the same directory!!
import sys
import re
from base_clauses import base_clauses

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

    clauses.extend(base_clauses)

    return clauses

'''
This function reads from STDIN and returns the unsolved sudoku puzzle
in an array. The wildcard values will be always changed to 0. 
'''
def get_puzzle():
    input_str = sys.stdin.read()
    puzzle = re.sub("[\n\r]", "", input_str)
    puzzle = [0 if char in [".", "?", "0", "*"] else int(char) for char in puzzle]
    return puzzle


def main():
    
    puzzle = get_puzzle()
    clauses = get_clauses(puzzle)

    # write to STDOUT
    print("p cnf {} {}".format(729 , len(clauses)))
    for clause in clauses:
        clause.append(0)
        print(*clause)


if __name__ == "__main__":
    main()