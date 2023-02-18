#!/usr/bin/env python3

import sys

'''
This function decodes the clause value to the corresponding
i, j, k values (i.e. row, column, and value of sudoku)
'''
def decode(value):
    value -= 1
    k = value % 9 + 1
    value //= 9
    j = value % 9 + 1
    value //= 9
    i = value + 1
    return i, j, k

'''
This function reads from STDIN and returns the solved sudoku puzzle
in an array
'''
def get_solution():
    input_str = sys.stdin.read()
    input = input_str.split(' ')

    sudoku = [[0 for i in range(9)] for j in range(9)]
    for sol in input:
        # get all those that do not start with '-'
        if sol[0] != '-' and sol.isnumeric():
            i, j, k = decode(int(sol))
            sudoku[i-1][j-1] = k
        
    return sudoku

def print_sudoku(sudoku):
    for i in range(9):
        for j in range(9):
            if j % 3 == 0 and j != 0:
                print(' ', end='')
            print(sudoku[i][j], end='')
        print()

if __name__ == "__main__":
   sudoku = get_solution()    
   print_sudoku(sudoku)
    
