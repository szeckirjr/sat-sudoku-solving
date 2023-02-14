#!/usr/bin/env python3

# STDIN must be in the same directory!!
import sys


def encode(i, j, k):
    return 81*(i - 1) + 9*(j - 1) + (k - 1) + 1

def get_clauses(puzzle):
    clauses = []
    unique_variables = set()

    # add clauses to enforce the given values in the sudoku puzzle
    for x in range(len(puzzle)):
        if puzzle[x] != 0:
            i = x // 9 + 1
            j = x % 9 + 1
            clauses.append([encode(i, j, puzzle[x])])
            unique_variables.add(encode(i, j, puzzle[x]))

    # every cell contains at least one number
    for i in range(1, 10):
        for j in range(1, 10):
            clauses.append([encode(i,j,k) for k in range(1,10)])
            unique_variables.add(encode(i,j,k) for k in range(1,10))

    # each number appears at most once in every row
    for i in range(1, 10):
        for k in range(1, 10):
            for j in range(1, 9):
                for l in range(j+1, 10):
                    clauses.append([-encode(i, j, k), -encode(i, l, k)])
                    unique_variables.add(encode(i, j, k))
                    unique_variables.add(encode(i, l, k))

    # each number appears at most once in every column
    for j in range(1, 10):
        for k in range(1, 10):
            for i in range(1, 9):
                for l in range(i+1, 10):
                    clauses.append([-encode(i, j, k), -encode(l, j, k)])
                    unique_variables.add(encode(i, j, k))
                    unique_variables.add(encode(l, j, k))

    # each number appears at most once in every 3x3 sub-grid
    # TODO

    num_variables = len(unique_variables)

    return clauses, num_variables

'''
This function reads from STDIN and returns the unsolved sudoku puzzle
in an array. The wildcard values will be always changed to 0. 
'''
def get_puzzle():
    input_str = sys.stdin.read()
    puzzle = input_str.replace("\n", "")
    puzzle = [0 if char in [".", "?", "0", "*"] else int(char) for char in puzzle]
    return puzzle


def main():
    
    puzzle = get_puzzle()
    clauses, num_variables = get_clauses(puzzle)

    # write to STDOUT
    print("p cnf {} {}".format(num_variables , len(clauses)))
    for clause in clauses:
        clause.append(0)
        print(*clause)


if __name__ == "__main__":
    main()
    
