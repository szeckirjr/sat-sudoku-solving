# SAT-based Sudoku Solving

## Project 1 - CSC322 Spring 2023

### Authors

Eduardo Szeckir
Rebecca Marshall
Emma Dewit
Sylvain Taghaoussi

## To Execute

The files under root are the compiled files. To run the program, execute the following command:

```bash
./hello
```

## To Compile

To compile the program, use the development files under `/source`.

A virtual environment is recommended. To create one, execute the following commands:

```bash
python3 -m venv venv
source venv/bin/activate
```

Install the dependencies

```bash
pip install -r requirements.txt
```

Compile the program

```bash
pyinstaller --onefile hello.py
```

To generate new requirements, execute the following commands:

```bash
pip freeze > requirements.txt
```
