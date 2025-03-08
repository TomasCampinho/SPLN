"""
Usage:
    ftk-ratio [OPTIONS] FILE1 FILE2

Options:
    --help        Show this help message.
"""

import sys
from collections import Counter

def calculate_ratio(freq1, freq2):
    ratio = {}
    for token in freq1:
        if token in freq2:
            ratio[token] = freq1[token] / freq2[token]
        else:
            ratio[token] = float('inf')
    return ratio

def print_ratios(ratios):
    for token, ratio in ratios.items():
        print(f"{token}: {ratio:.3f}")

def read_frequencies(file_path):
    frequencies = {}
    with open(file_path, 'r') as file:
        for line in file:
            token, freq = line.strip().split()
            frequencies[token] = float(freq)
    return frequencies

def main():
    if "--help" in sys.argv or len(sys.argv) != 3:
        print(__doc__)
        sys.exit(0)
    
    file1, file2 = sys.argv[1], sys.argv[2]
    
    freq1 = read_frequencies(file1)
    freq2 = read_frequencies(file2)
    
    ratios = calculate_ratio(freq1, freq2)
    print_ratios(ratios)

if __name__ == "__main__":
    main()
