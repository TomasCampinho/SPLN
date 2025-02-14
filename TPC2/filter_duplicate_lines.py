#!/usr/bin/env python3
"""
Filter duplicate lines from a text file.

Usage: ./filter_duplicate_lines.py [OPTIONS] FILE

Options:
  default (no options)    Removes all duplicate non-empty lines
  -e                      Also removes duplicate empty lines
  -c                      Comments out duplicate lines instead of removing them outright
"""

from jjcli import *

def filter_duplicate_lines(lines, comment=False, remove_empty=False):
    seen = set()
    result = []
    
    for line in lines:
        stripped_line = line.strip()
        
        if stripped_line == '' and not remove_empty:    # keep all empty lines by default
            result.append(line)
        else:
            if stripped_line not in seen:
                    result.append(line)
                    seen.add(stripped_line)
            elif comment:   # option to comment out duplicate lines
                result.append(f"# {line}")

    return result

def main():
    if "--help" in sys.argv:
        print(__doc__)
        sys.exit(0)

    cl = clfilter("ce")
    opts = cl.opt
    args = cl.args 

    if not args:
        print("Error: No input file provided.", file=sys.stderr)
        print(__doc__)
        sys.exit(1)

    input_file = args[0]

    with open(input_file, 'r') as f:
        lines = f.readlines()

    processed_lines = filter_duplicate_lines(
        lines,
        comment='-c' in opts, 
        remove_empty='-e' in opts
    )

    for line in processed_lines:
        print(line, end='')

if __name__ == "__main__":
    main()
