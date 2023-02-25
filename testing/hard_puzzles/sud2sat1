#!/usr/bin/env python3

import sys
import re
import os

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

    return clauses

'''
This function reads from STDIN and returns the unsolved sudoku puzzle
in an array 
'''
def get_puzzles():
    input_str = sys.stdin.read()
    puzzles = input_str.split('\n')
    return puzzles

def create_output_folder(new_dir):
    if not os.path.exists(new_dir):
        os.makedirs(new_dir)

def solve_puzzle(puzzle, index):
    puzzle = [0 if char in [".", "?", "0", "*"] else int(char) for char in puzzle]
    clauses = get_clauses(puzzle)

    create_output_folder('hard_puzzle_output/')

    with open("hard_puzzle_output/puzzle_{}.cnf".format(index), "w") as file:
        file.write("p cnf {} {}\n".format(729 , len(clauses)))
        for clause in clauses:
            clause.append(0)
            file.write("{}\n".format(" ".join(str(x) for x in clause)))


if __name__ == "__main__":
    puzzles = get_puzzles()
    index = 1

    for puzzle in puzzles:
        solve_puzzle(puzzle, index)
        index += 1
    
