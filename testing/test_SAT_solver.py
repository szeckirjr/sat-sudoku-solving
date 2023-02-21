#!/usr/bin/env python3

import os
import shutil
import sys

# copy file to this folder
def copy_file(src_path, dst_path="."):
    try:
        shutil.copy(src_path, dst_path)
    except IOError as e:
        print(f"Unable to copy file. {e}")

# delete file
def delete_file(file_path):
    try:
        os.remove(file_path)
    except OSError as e:
        print(f"Error: {file_path} : {e.strerror}")


def run_sud2sat(puzzle, i):
    output_file = "puzzle_{}.cnf".format(i)

    # Run sud2sat
    os.system(f"./sud2sat < {puzzle} > {output_file}")


def run_minisat(i, output_folder_path): 
    input_file = "puzzle_{}.cnf".format(i)
    assign_file = "assign_{}.txt".format(i)
    stat_file = "{}/stat_{}.txt".format(output_folder_path, i)

    # Run the minisat command and capture the output in a file
    os.system(f"minisat {input_file} {assign_file} > {stat_file}")

    # Delete input and assign file
    delete_file(input_file)
    delete_file(assign_file)


def create_output_folder(new_dir):
    if not os.path.exists(new_dir):
        os.makedirs(new_dir)


# Run all puzzles with minisat
def process_puzzles(folder_path):
    create_output_folder("test_output/")
    file_index = 1

    for file_name in os.listdir(folder_path):
        if file_name.endswith('.txt'):
            file_path = os.path.join(folder_path, file_name)
            copy_file(file_path) # copy puzzle file to current directory
            run_sud2sat(file_name, file_index)
            run_minisat(file_index, "test_output/")
            delete_file(file_name) # remove puzzle file from current directory
            file_index += 1

def parse_args():
    if len(sys.argv) != 2:
        print("Please provide one argument")
    else:
        return sys.argv[1]

if __name__ == '__main__':
    folder_path = parse_args()
    process_puzzles(folder_path)
    
