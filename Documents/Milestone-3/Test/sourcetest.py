'''
    Checks to see if a production repository has 
    at least 50% of code from a given development 
    branch.
    Usage:

        python3 sourcetest.py /prod/ /dev/

'''

import filecmp
import difflib
import os
import sys

def compare_directories(directory1, directory2):
    directory_comparison = filecmp.dircmp(directory1, directory2)

    for common_file in directory_comparison.common_files:
        file1 = os.path.join(directory1, common_file)
        file2 = os.path.join(directory2, common_file)

        if filecmp.cmp(file1, file2):
            print(f"PASS: {common_file} (Identical)")
        else:
            similarity = compare_files(file1, file2)
            if similarity > 0.5:
                print(f"PASS: {common_file} (Similarity: {similarity * 100:.2f}%)")

def compare_files(file1, file2):
    with open(file1, 'r') as f1, open(file2, 'r') as f2:
        text1 = f1.read()
        text2 = f2.read()

    d = difflib.Differ()
    text1_lines = text1.splitlines()
    text2_lines = text2.splitlines()

    # Calculate the similarity ratio
    sm = difflib.SequenceMatcher(None, text1_lines, text2_lines)
    return sm.ratio()

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Error, usage is: python3 sourcetest.py /prod/ /dev/")
        sys.exit(1)

    dir1 = sys.argv[1]
    dir2 = sys.argv[2]

    compare_directories(dir1, dir2)