#!/usr/bin/env python3

import os
import shutil
import sys
import csv
import argparse

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


def run_sud2sat(sud2sat_path, puzzle, i):
    output_file = "puzzle_{}.cnf".format(i)
    sud2sat = os.path.basename(sud2sat_path)

    # Run sud2sat
    os.system(f"./{sud2sat} < {puzzle} > {output_file}")


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
def process_puzzles(folder_path, output_folder, stat_output_folder, sud2sat_path):    
    create_output_folder(stat_output_folder)
    copy_file(sud2sat_path)
    copy_file(sud2sat_path, output_folder)
    file_index = 1

    for file_name in os.listdir(folder_path):
        if file_name.endswith('.txt'):
            file_path = os.path.join(folder_path, file_name)
            copy_file(file_path) # copy puzzle file to current directory
            run_sud2sat(sud2sat_path, file_name, file_index)
            run_minisat(file_index, stat_output_folder)
            delete_file(file_name) # remove puzzle file from current directory
            file_index += 1

    delete_file(os.path.basename(sud2sat_path))

def get_average_stat(total_num_files, total_num_var):
    sum = 0.0
    for val in total_num_var:
        sum += val

    return sum/total_num_files

def parse_statistics(stat_folder, output_file):
    num_files = len(os.listdir(stat_folder))

    # initialize variables to hold the statistics
    total_num_vars = []
    total_num_clauses = []
    total_parse_time = []
    total_simp_time = []
    total_num_restarts = []
    total_num_conflicts = []
    total_num_decisions = []
    total_num_propagations = []
    total_memory_used = []
    total_cpu_time = []
    satisfiable_cnt = 0

    for input_file in os.listdir(stat_folder):
        if input_file.endswith('.txt'):
            file_path = os.path.join(stat_folder, input_file)
            # open the input file
            with open(file_path, 'r') as f:
                # read the lines of the input file
                lines = f.readlines()

            # parse the statistics from the input file
            for line in lines:
                if line.startswith('|  Number of variables:'):
                    total_num_vars.append(int(line.replace('|','').split(':')[1].strip()))
                elif line.startswith('|  Number of clauses:'):
                    total_num_clauses.append(int(line.replace('|','').split(':')[1].strip()))
                elif line.startswith('|  Parse time:'):
                    total_parse_time.append(float(line.replace('|','').split(':')[1].replace('s','').strip()))
                elif line.startswith('|  Simplification time:'):
                    total_simp_time.append(float(line.replace('|','').split(':')[1].replace('s','').strip()))
                elif line.startswith('restarts'):
                    total_num_restarts.append(float(line.replace('|','').split(':')[1].strip()))
                elif line.startswith('conflicts'):
                    total_num_conflicts.append(float(line.replace('|','').split(':')[1].split('(')[0].strip()))
                elif line.startswith('decisions'):
                    total_num_decisions.append(float(line.replace('|','').split(':')[1].split('(')[0].strip()))
                elif line.startswith('propagations'):
                    total_num_propagations.append(float(line.replace('|','').split(':')[1].split('(')[0].strip()))
                elif line.startswith('Memory used'):
                    total_memory_used.append(float(line.replace('|','').split(':')[1].replace('MB', '').strip()))
                elif line.startswith('CPU time'):
                    total_cpu_time.append(float(line.replace('|','').split(':')[1].replace('s','').strip()))
                elif line.startswith('SATISFIABLE'):
                    satisfiable_cnt += 1

    # get average stats
    num_vars = get_average_stat(num_files, total_num_vars)
    num_clauses = get_average_stat(num_files, total_num_clauses)
    parse_time = get_average_stat(num_files, total_parse_time)
    simp_time = get_average_stat(num_files, total_simp_time)
    num_conflicts = get_average_stat(num_files, total_num_conflicts)
    num_restarts = get_average_stat(num_files, total_num_restarts)
    num_decisions = get_average_stat(num_files, total_num_decisions)
    num_propagations = get_average_stat(num_files, total_num_propagations)
    memory_used = get_average_stat(num_files, total_memory_used)
    cpu_time = get_average_stat(num_files, total_cpu_time)

    # get worst case stat
    num_vars_wc = max(total_num_vars)
    num_clauses_wc = max(total_num_clauses)
    parse_time_wc = max(total_parse_time)
    simp_time_wc = max(total_simp_time)
    num_conflicts_wc = max(total_num_conflicts)
    num_restarts_wc = max(total_num_restarts)
    num_decisions_wc = max(total_num_decisions)
    num_propagations_wc = max(total_num_propagations)
    memory_used_wc = max(total_memory_used)
    cpu_time_wc = max(total_cpu_time)


    # write the statistics to the output file as a CSV
    with open(output_file, 'w', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(['', 'Average Case Statistics', 'Worst Case Statistics'])
        writer.writerow(['Number of variables', num_vars, num_vars_wc])
        writer.writerow(['Number of clauses', num_clauses, num_clauses_wc])
        writer.writerow(['Parse time (s)', parse_time, parse_time_wc])
        writer.writerow(['Simplification time (s)', simp_time, simp_time_wc])
        writer.writerow(['Number of conflicts', num_conflicts, num_conflicts_wc])
        writer.writerow(['Number of restarts', num_restarts, num_restarts_wc])
        writer.writerow(['Number of decisions', num_decisions, num_decisions_wc])
        writer.writerow(['Number of propagations', num_propagations, num_propagations_wc])
        writer.writerow(['Memory used (MB)', memory_used, memory_used_wc])
        writer.writerow(['CPU time (s)', cpu_time, cpu_time_wc])
        writer.writerow(['','',''])
        writer.writerow(['Number of satisfiable puzzles', satisfiable_cnt])
        writer.writerow(['Number of unsatisfiable puzzles', num_files-satisfiable_cnt])
    
def parse_args(args):
    parser = argparse.ArgumentParser()
    parser.add_argument("input", help="Input folder with puzzle files")
    parser.add_argument("-s", "--sud2sat", help="Path to sud2sat executable")
    parser.add_argument("-o", "--output", help="output folder for stats and report file", default="test_output/")
    p_args = parser.parse_args(args)
    return p_args

if __name__ == '__main__':
    args = parse_args(sys.argv[1:])
    stat_output_folder = args.output + 'stat_files/'
    output_file = args.output + 'ac_and_wc_stats.csv'
    process_puzzles(args.input, args.output, stat_output_folder, args.sud2sat)
    parse_statistics(stat_output_folder, output_file)
    
