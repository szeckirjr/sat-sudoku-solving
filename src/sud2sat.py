#!/usr/bin/env python3
import sys


def encode(i, j, k):
    return 81*(i - 1) + 9*(j - 1) + (k - 1) + 1

def get_clauses():
    return

'''
This function opens the file and returns the unsolved sudoku puzzle
into an array. The wildcard values will be always changed to 0. 
'''
def getfilecontents(path):
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
    
    puzzle = getfilecontents(path)
    print("Puzzle from input:\n", puzzle, "\n")
    clauses = get_clauses()
    clauses = [[1,3,4,5], [14,6,3], [944, 5]] # testing
    
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
    
