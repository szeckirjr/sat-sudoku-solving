#!/usr/bin/env python3

import sys
import re


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
    for k in range(1, 10):
        for a in range(0, 3):
            for b in range(0, 3):
                for u in range(1, 4):
                    for v in range(1, 3):
                        for w in range(v+1, 4):
                            clauses.append([-encode(3*a+u, 3*b+v, k), -encode(3*a+u, 3*b+w, k)])

    for k in range(1, 10):
        for a in range(0, 3):
            for b in range(0, 3):
                for u in range(1, 3):
                    for v in range(1, 4):
                        for w in range(u+1, 4):
                            for t in range(1, 4):
                                clauses.append([-encode(3*a+u, 3*b+v, k), -encode(3*a+w, 3*b+t, k)])

    # there is at most one number in each cell
    for i in range(1, 10):
        for j in range(1, 10):
            for k in range(1,9):
                for l in range(k+1, 10):
                    clauses.append([-encode(i, j, k), -encode(i, j, l)])
        


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
    
