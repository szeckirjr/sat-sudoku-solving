# SAT-based Sudoku Solving

## Project 1 - CSC322 Spring 2023

### Authors


| Name               | V#               |
| ----------------   | ---------------- |
| Eduardo Szeckir    | V009221126       |
| Rebecca Marshall   | V00911412        |
| Emma Dewit         | V00906515        |
| Sylvain Taghaoussi |                  |

## To Execute

The files under root are the compiled files. To run the program, execute the following command:

```bash
./sud2sat <puzzle.txt >puzzle.cnf
minisat puzzle.cnf assign.txt >stat.txt
./sat2sud <assign.txt >solution.txt
```

NOTE: sud2sat1 uses a different input format. The output folder is hardcoded to `hard_puzzle_output/`. To run sud2sat1, execute the following command:

```bash
./sud2sat1 <hard_puzzle/hard_puzzles.txt
```

## To Compile

To make the program executable on Unix systems, needed for the lab:

1. Make sure the following line is at the top of the `.py` file:

```python
#!/usr/bin/env python3
```

2. Copy the file into the root directory of the project:

```bash
cp hello.py ./../hello
```

3. Run the following command to make file executable:

```bash
chmod +x hello
```

4. Run the program with the following command:

```bash
./hello
```

## Common Errors
```bash
-bash: ./hello: Permission denied
```

To fix error, run the following command:
```bash
chmod +x hello
```

## Performance Analysis
A performance analysis can be conducted on the different sud2sat programs using `testing/test_SAT_solver` program. It provides a report of the worst and average case statistics. Run `./test_SAT_solver -h` for help.
