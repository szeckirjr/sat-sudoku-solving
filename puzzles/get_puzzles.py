import re

# get the puzzles from p096_sudoku.txt file
with open('../p096_sudoku.txt', 'r') as f:
    data = f.read()

# split the input data into separate puzzles
puzzles = re.split(r'Grid \d+', data)[1:]

# save each puzzle to its own text file
for i, puzzle in enumerate(puzzles):
    
    filename = f'puzzle_{i+1:02}.txt'
    
    with open(filename, 'w') as f:
        f.write(puzzle.strip())
        
    print(f'Saved {filename}')