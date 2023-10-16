'''
    Checks to see if a production repository has 
    at least 50% of code from tests.py
    Usage:

        python3 sourcetest.py /prod/ /dev/

'''


import sys

import os
import glob

def count_lines_in_file(file_path):
    with open(file_path, 'r') as file:
        return len(file.readlines())

def main(project_directory):
    source_file_count = 0
    source_file_lines = 0

    for root, dirs, files in os.walk(project_directory):
        for file in files:
            if file.endswith(".py"):
                source_file_count += 1
                source_file_lines += count_lines_in_file(os.path.join(root, file))

    tests_file = os.path.join(project_directory, 'tests.py')

    if source_file_count == 0:
        return False  # No source files in the project

    if not os.path.exists(tests_file):
        return False  # No tests.py file in the project

    tests_lines = count_lines_in_file(tests_file)

    return tests_lines >= 0.5 * (source_file_lines / source_file_count)

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Error, usage is: python3 sourcetest.py /prod/")
        sys.exit(1)

    dirName = sys.argv[1]
    result = main(dirName)
    print(result)