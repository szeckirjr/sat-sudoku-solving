#!/usr/bin/env python3
import sys


def encode(i, j, k):
    return 81*(i - 1) + 9*(j - 1) + (k - 1) + 1

def get_clauses():
    return

def main(sud):
    clauses = get_clauses()
    clauses = [[1,3,4,5], [14,6,3], [944, 5]] # testing
    
    print("p cnf {} {}".format("<# variables>" , len(clauses)))
    for clause in clauses:
        clause.append(0)
        print(*clause)


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
    