#!/usr/bin/env python3
import sys


def encode(i, j, k):
    return 81*(i - 1) + 9*(j - 1) + (k - 1) + 1

def get_clauses():
    return

# This function opens the file and returns the data
# returns sudoku puzzles in following format
# all puzzles are stored in a list, puzzles = []
# individual puzzles are stored in one list with len 81
# the list is of len 81 for each square of a 9x9 sudoku puzzle
def getfilecontents(path):
    try:
        f = open(path, "r")
        content = f.read()
        puzzles = []
        puzzle = []
        index = 0
        for char in content:
            # if puzzle isn't complete and reached end of file
            if index == len(content) - 1 and len(puzzle) < 81:
                for i in range(0, 81-len(puzzle)):
                    puzzle.append(0)
                puzzles.append(puzzle)
                puzzle = []
                break

            # check if puzzle is full, if it is push to puzzles list and empty it
            if len(puzzle) >= 81:
                puzzles.append(puzzle)
                puzzle = []
            # if entry is num append integer version of char num            
            if char in ["1", "2", "3", "4", "5", "6", "7", "8" , "9"]:
                puzzle.append(int(char))
            # if wildcard character push 0
            elif char in [".", "?", "0", "*"]:
                puzzle.append(0)
            index += 1
        return puzzles

    except Exception as err:
        print(f"Failed to parse from {path}")
        print(err)
        sys.exit(2)
    return
    

def main(path):
    
    puzzles = getfilecontents(path)
    print("Puzzles from input:\n", puzzles, "\n")
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
    
