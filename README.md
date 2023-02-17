# SAT-based Sudoku Solving

## Project 1 - CSC322 Spring 2023

### Authors

Eduardo Szeckir
Rebecca Marshall
Emma Dewit V00906515
Sylvain Taghaoussi

## To Execute

The files under root are the compiled files. To run the program, execute the following command:

```bash
./sud2sat <puzzle.txt >puzzle.cnf
minisat puzzle.cnf assign.txt >stat.txt
./sat2sud <assign.txt >solution.txt
```

## To Compile

To make the program executable on Unix systems, needed for the lab:

1. Make sure the following line is at the top of the `.py`file:

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
